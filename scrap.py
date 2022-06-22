class Scrapping(object):
    @staticmethod
    def extract_experience(exp):
        bag = []
        for i in range(len(exp["experience"])):
            try:
                title = exp["experience"][i]["title"]
            except KeyError:
                title = ""
            try:
                local = exp["experience"][i]["companyName"]
            except KeyError:
                local = ""
            try:
                start_date = exp["experience"][i]["timePeriod"]["startDate"]
            except KeyError:
                start_date = ""
            try:
                end_date = exp["experience"][i]["timePeriod"]["endDate"]
            except KeyError:
                end_date = ""
            try:
                city = exp["experience"][i]["geoLocationName"].split(",")[0]
            except:
                city = ""
            try:
                country = exp["experience"][i]["geoLocationName"].split(",")[1]
            except:
                country = ""
            try:
                description = exp["experience"][i]["description"]
            except KeyError:
                description = ""

            res = {
                "title": title,
                "local": local,
                "start_date": start_date,
                "end_date": end_date,
                "city": city,
                "state": "",
                "country": country,
                "description": description,
            }
            bag.append(res)
        return bag

    @staticmethod
    def extract_academic(exp):
        bag = []
        for i in range(len(exp["education"])):
            try:
                institution = exp["education"][i]["schoolName"]
            except KeyError:
                institution = ""
            try:
                course = exp["education"][i]["fieldOfStudy"]
            except KeyError:
                course = ""
            try:
                start_date = exp["education"][i]["timePeriod"]["startDate"]
            except KeyError:
                start_date = ""
            try:
                end_date = exp["education"][i]["timePeriod"]["endDate"]
            except KeyError:
                end_date = ""
            res = {
                "institution": institution,
                "course": course,
                "start_date": start_date,
                "end_date": end_date,
            }
            bag.append(res)
        return bag

    @staticmethod
    def extract_contact(info):
        try:
            email = info["email_address"]
        except KeyError:
            email = ""
        try:
            websites = info["websites"]
        except KeyError:
            websites = ""
        try:
            twitter = info["twitter"]
        except KeyError:
            twitter = ""
        try:
            birth = info["birthdate"]
        except KeyError:
            birth = ""
        try:
            ims = info["ims"]
        except KeyError:
            ims = ""
        try:
            phone = info["phone_numbers"]
        except KeyError:
            phone = ""
        res = {
            "email_address": email,
            "websites": websites,
            "twitter": twitter,
            "birth": birth,
            "ims": ims,
            "phone_numbers": phone,
        }
        return res

    @staticmethod
    def extract_skills(skills):
        return skills

    @staticmethod
    def extract_volunteer(exp):
        bag = []
        for i in range(len(exp["volunteer"])):
            try:
                local = exp["volunteer"][i]["companyName"]
            except KeyError:
                local = ""
            try:
                description = exp["volunteer"][i]["description"]
            except KeyError:
                description = ""
            try:
                start_date = exp["volunteer"][i]["timePeriod"]["startDate"]
            except KeyError:
                start_date = ""
            try:
                end_date = exp["volunteer"][i]["timePeriod"]["endDate"]
            except KeyError:
                end_date = ""
            try:
                activity = exp["volunteer"][i]["role"]
            except KeyError:
                activity = ""
            res = {
                "local": local,
                "description": description,
                "start_date": start_date,
                "end_date": end_date,
                "activity": activity,
            }
            bag.append(res)
        return bag

    @staticmethod
    def extract_name(exp):
        try:
            name = exp["firstName"] + " " + exp["lastName"]
        except:
            name = ""
        return name

    @staticmethod
    def extract_headline(exp):
        try:
            headline = exp["headline"]
        except:
            headline = ""
        return headline

    @staticmethod
    def extract_summary(exp):
        try:
            summary = exp["summary"]
        except:
            summary = ""
        return summary

    @staticmethod
    def extract_city(exp):
        try:
            city = exp["geoLocationName"].split(",")[0]
        except:
            city = ""
        return city

    @staticmethod
    def extract_state(exp):
        try:
            state = exp["geoLocationName"].split(",")[1]
        except:
            state = ""
        return state

    @staticmethod
    def extract_country(exp):
        try:
            country = exp["locationName"]
        except:
            country = ""
        return country


class BuildResponse(object):
    @staticmethod
    def process(exp, info, skill):
        js = {
            "status_sge": "",
            "name": Scrapping().extract_name(exp),
            "last_query": "",
            "activity_linkedin": Scrapping().extract_headline(exp),
            "Looking_job": "",
            "city": Scrapping().extract_city(exp),
            "state": Scrapping().extract_state(exp),
            "country": Scrapping().extract_country(exp),
            "contact_info": Scrapping().extract_contact(info),
            "about_me": Scrapping().extract_summary(exp),
            "experience": Scrapping().extract_experience(exp),
            "academic": Scrapping().extract_academic(exp),
            "skills": Scrapping().extract_skills(skill),
            "volunteer_work": Scrapping().extract_volunteer(exp),
        }
        return js
