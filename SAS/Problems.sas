Data Group;
    length CRN $9 STUDENTiD $9 STUDENT_NAME $40 ;
    Infile datalines delimiter=",";
    Input GROUPID STUDENT_NAME $ STUDENTiD $ CRN $;
    datalines;
1,DARIO MEDINA,932005123, CRN-00000
2,TIM,932000800, CRN-00000
;

/**************************/
/*Macro definitions */
/**************************/

%macro CH_02_PRB_01;

   /* Code for problem #01  here */
  
    proc optmodel;
    var X1, X2;
    num prob_id init 1;  /*PROB id*/
    max z = 40*X1 + 50*X2;
    con
    X1 + 2*X2 <= 40,
    4*X1 + 3*X2 <= 120,
    X1 >=0, X2 >= 0;
    solve;
    create data sol_data_01 from X1 X2 prob_id;
    
    print X1 X2;


    proc sql;
    create table sol_PRB_01 as
        select  
            Group.*
            ,sol_data_01.*
    
        from sol_data_01,
            Group;
    quit;

   
%mend CH_02_PRB_01;

%macro CH_02_PRB_02;

   /* Code for problem #01  here */
  
    proc optmodel;
    var X1, X2;
    num prob_id init 2;     /*PROB id*/
    max z = 40*X1 + 50*X2;
    con
    X1 + 2*X2 <= 40,
    4*X1 + 3*X2 <= 120,
    X1 >=0, X2 >= 0;
    solve;
    create data sol_data_01 from X1 X2 prob_id;
    
    print X1 X2;


    proc sql;
    create table sol_PRB_02 as
        select  
            Group.*
            ,sol_data_01.*
    
        from sol_data_01,
            Group;
    quit;

   
%mend CH_02_PRB_02;

/**************************/
/*End of macro definitions */
/**************************/



/**************************/
/*Calls to macros  */
/**************************/

%CH_02_PRB_01;
%CH_02_PRB_02;

/**************************/
/*Submit the following dataset into Blackboard  */
/**************************/

DATA sol_PRB ; SET sol_PRB_01 sol_PRB_02; RUN;
proc print data = sol_PRB; run;


