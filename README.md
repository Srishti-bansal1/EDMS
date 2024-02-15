# Emplyee Details

# Introduction <br>
This is a employee details management system project. In this project I used python language (version 3.9 ) & Django Rest framework (version 4.2.9). This project  used to created employee details, read the employee information, update the informations and delete the details. 
 <br>
In this project, I designed a model and their fields are name, roll_no, email, manager. Manager field related with Foreign key. Migrated the model to create a Table. Connected with MYSQL database. Created APIs for Create, Read, Update and Delete operation. <br>

`http://127.0.0.1:8000/edms/Edms/show` use for read <br> `http://127.0.0.1:8000/edms/Edms/create` use for create <br> `http://127.0.0.1:8000/edms/Edms/<id>/modify` use for update <br> `http://127.0.0.1:8000/edms/Edms/delete_all` use for delete all registration. 
<br>
In this project, I also designed one more model which is connected to 1st model with foreign key and their fields are emp_model_id, state, city, pin. Created APIs for Create, Read, Update and Delete operation. <br>

`http://127.0.0.1:8000/Eadd/emp_add/show` use for read <br> `http://127.0.0.1:8000/Eadd/emp_add/add_create` use for create <br> `http://127.0.0.1:8000/Eadd/emp_add/<id>/modify` use for update <br> `http://127.0.0.1:8000/Eadd/emp_add/delete_all` use for delete all registration. 
<br>
In this project, I used pagination concept, ModelSerializer & MethodSerializer concept and class based viewset & function based view concept and router for urls.

# SetUp for Linux or MAC <br>
step 1 : open terminal and clone the code by executing *git clone <https://github.com/Srishti-bansal1/EDMS>*
<br>
step 2 : Install virtual environment  with command : pip install virtualenv
<br>
step 3 : Activate the virtual environment with command : source  .venv/bin/activate
<br>
step 4 : Move in projct file with command : cd EDMSpro
<br>
step 5 : Execute migration command to create table in database using command : python mange.py migrate
<br>
step 6 : Run the server with command : python manage.py runserver 8000
<br>

# API Documentation -<br>
        1. Create :- End point - http://127.0.0.1:8000/edms/Edms/create
                     request body - {	
                                        "name"   : <str> ,
                                        "roll_no": <str>,
                                        "email"  : <str>,
                                        "state"  : <str> ,
                                        "city"   : <str> ,
                                        "pin"    : <int>
                                        }	
                     response body - {	
                                        "id "    : <int>,
                                        "name"   : <str> ,
                                        "dob"    : <str>,
                                        "email"  : <str>,
                                        "state"  : <str> ,
                                        "city"   : <str> ,
                                        "pin"    : <int>
                                        }
                                    	

        2. i) Read :- End point - http://127.0.0.1:8000/emp_all/emp_all_detail/get_all_emp
        
        
                   response body - {	
                                        "id "    : <int>,
                                        "name"   : <str> ,
                                        "roll_no": <str>,
                                        "email"  : <str>,
                                        "state"  : <str> ,
                                        "city"   : <str> ,
                                        "pin"    : <int>
                                        }	
        
            ii) Read using pagination :- End point - http://127.0.0.1:8000/edms/Edms/show_null_id?page=${page_no}&page_size=${page_size_no}
                      response body - {	
                                        "id "    : <int>,
                                        "name"   : <str> ,
                                        "roll_no": <str>,
                                        "email"  : <str>,
                                        "state"  : <str> ,
                                        "city"   : <str> ,
                                        "pin"    : <int>
                                        }	

        3. Update :-  End point - http://127.0.0.1:8000/edms/Edms/<id>/modify
        
                      request body - {	
                                        "name"   : <str> ,
                                        "roll_no": <str>,
                                        "email"  : <str>,
                                        "state"  : <str> ,
                                        "city"   : <str> ,
                                        "pin"    : <int>
                                        }	
                                    
                      response body - {	
                                        "id "    : <int>,
                                        "name"   : <str> ,
                                        "roll_no": <str>,
                                        "email"  : <str>,
                                        "state"  : <str> ,
                                        "city"   : <str> ,
                                        "pin"    : <int>
                                        }	       
                                                     
        
        4. Delete :- End point - http://127.0.0.1:8000/Eadd/emp_add/delete
    
                     response body - empty
