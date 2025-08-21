
# convert to big letter
text = """
SET SERVEROUTPUT ON;

DECLARE 
    c_max_score CONSTANT NUMBER := 100;
    v_score NUMBER := 60;
    l_grade VARCHAR2(20);
BEGIN
    <<f_statement>>
    IF v_score IS NULL THEN
        DBMS_OUTPUT.PUT_LINE('Score not available.');
        RETURN;
    ELSIF v_score > c_max_score THEN
        DBMS_OUTPUT.PUT_LINE('Invalid score.');
        GOTO second_statement;
    ELSIF v_score = 0 THEN
        DBMS_OUTPUT.PUT_LINE('No performance data.');
    END IF;

    <<second_statement>>
    CASE 
        WHEN v_score >= 90 AND v_score <= 100 THEN
            l_grade := 'Excellent';
        WHEN v_score >= 75 AND v_score <= 89 THEN
            l_grade := 'Very Good';
        WHEN v_score >= 60 AND v_score <= 74 THEN
            l_grade := 'Good';
        WHEN v_score >= 40 AND v_score <= 59 THEN
            l_grade := 'Average';
        WHEN v_score < 40 THEN
            l_grade := 'Poor';
        ELSE
            l_grade := 'Invalid';
    END CASE;
    
    DBMS_OUTPUT.PUT_LINE('Result is: ' || l_grade);
END;

"""
lowercase_text = text.lower()
print(lowercase_text)




