# linkedin-scrapper-api
Linkedin Scrapper based on Linkedin-API module

# How to use
### Credentials
Insert your login info on credentials.yml file.
> login: "fulano@gmail.com"
> password: password

### Profile list
Insert your profile list on data.csv file and modify the path on credentials.yml
> csv:
>   file: "file path.csv"

### Script
> python request-linkedin.py


# Dependencies
linkedin_api
> pip3 install linkedin-api~=2.0.0a

yaml
> pip install pyyaml

pandas
> pip install pandas

json
>pip install json
