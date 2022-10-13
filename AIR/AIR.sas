/* libname is magid, imported csv files attributes, intent and ratings as a, i, r */
libname magid "/home/u50061083/Capstone";

proc import datafile='/home/u50061083/Capstone/student_movie_attributes.csv' 
        DBMS=CSV OUT=magid.a REPLACE;
    GETNAMES=YES;
    GUESSINGROWS=1000;

proc import datafile='/home/u50061083/Capstone/student_movie_intent.csv' 
        DBMS=CSV OUT=magid.i REPLACE;
    GETNAMES=YES;
    GUESSINGROWS=1000;

proc import datafile='/home/u50061083/Capstone/student_movie_ratings.csv' 
        DBMS=CSV OUT=magid.r REPLACE;
    GETNAMES=YES;
    GUESSINGROWS=15000;
RUN;

/* Setting new dataset names as (a, i, r) and DROP duplicate columns */
data a;
    set magid.a;
    drop etl_run_guid intent_score survey_date content_type movie_name 
        household_size gender_name age_group_bracket ethnicity_name;
        
data i;
    set magid.i;
    drop etl_run_guid;
    
data r;
    set magid.r;
    drop etl_run_guid networks content_type;
run;

    /* SORT files by respondent_id then by movie_id */
proc sort data=a;
    by respondent_id movie_id;
    
proc sort data=i;
    by respondent_id movie_id;
    
proc sort data=r;
    by respondent_id movie_id;
run;

    /* merge all three datasets */
data air;
    merge r i a;
    by respondent_id movie_id;
run;