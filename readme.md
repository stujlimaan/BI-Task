#Route
1. /login POST
    {
	    "email":"tujliman1999@gmail.com",
	    "password":123
    }

2. /signup POST
    {
	    "email":"tujliman1999@gmail.com",
	    "password":123
        "user_type":"ADMIN" OR "OWNER" OR "USER"
    }
3. /user GET 
    #ADD TOKEN IN Authorization HEADER 

4. /admin GET
    #ADD TOKEN IN Authorization HEADER 

5. /owner GET 
    #ADD TOKEN IN Authorization HEADER 
