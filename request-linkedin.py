from linkedin_api import Linkedin
import json
import yaml
import scrap
import pandas as pd


credential_path = "credentials.yml"


class Credentials(object):
    def __init__(self, credential_path):
        with open(credential_path, "r") as file:
            self.credentials = yaml.safe_load(file)

    def get_credentials(self):
        return self.credentials


class RequestLinkedin(Credentials):
    def __init__(self, credential_path):
        super().__init__(credential_path)
        self.user = self.credentials["credentials"]["user"]
        self.password = self.credentials["credentials"]["password"]

    def login(self):
        # Debug login
        # print(f'login:{str(self.user)} \npassword:{str(self.password)}')
        try:
            login = Linkedin(self.user, self.password)
        except:
            print("Falha no Login.")
            raise
        return login


class GetProfileInfo(object):
    @staticmethod
    def profile(login, link):
        data = login.get_profile(link)
        return data

    @staticmethod
    def ContactInfo(login, link):
        data = login.get_profile_contact_info(link)
        return data

    @staticmethod
    def skills(login, link):
        data = login.get_profile_skills(link)
        return data


login = RequestLinkedin(credential_path).login()


if __name__ == "__main__":
    # load profile list
    data = pd.read_csv(Credentials(credential_path).get_credentials()["csv"]["file"])
    for profile in data["link"]:
        # Search and extract info
        info_request = GetProfileInfo().profile(login, profile)
        contact_request = GetProfileInfo().ContactInfo(login, profile)
        skill_request = GetProfileInfo().skills(login, profile)
        res = scrap.BuildResponse().process(
            info_request, contact_request, skill_request
        )
        #

        # Save json
        with open(f"{profile}.json", "w") as outfile:
            json.dump(res, outfile, ensure_ascii=False)
