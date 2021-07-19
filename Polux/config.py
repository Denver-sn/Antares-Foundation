import requests
from bs4 import BeautifulSoup as bs

r = requests.get("https://indextracker.ga/")


contenuto = bs(r.text, "html.parser")

index_health_ten = contenuto.find("th").findNext("th").findNext("th").findNext("td")
index_health_nine = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td")
index_health_eight = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext("td")
index_health_seven = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td")
index_health_six = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td")
index_health_five = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td")
index_health_four = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td")
index_health_three = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td")
index_health_two = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td")
index_health_one = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td")

health = str("\n❤Health Index\n\n" +
             "10 --> " + index_health_ten.get_text() + "\n" +
             "9 --> " + index_health_nine.get_text() + "\n" +
             "8 --> " + index_health_eight.get_text() + "\n" +
             "7 --> " + index_health_seven.get_text() + "\n" +
             "6 --> " + index_health_six.get_text() + "\n" +
             "5 --> " + index_health_five.get_text() + "\n" +
             "4 --> " + index_health_four.get_text() + "\n" +
             "3 --> " + index_health_three.get_text() + "\n" +
             "2 --> " + index_health_two.get_text() + "\n" +
             "1 --> " + index_health_one.get_text() + "\n\n By @Denver02"

             )

####---- Military
index_military_ten = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td")
index_military_nine = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td")
index_military_eight = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td")
index_military_seven = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td")
index_military_six = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td")
index_military_five = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td")
index_military_four = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td")
index_military_three = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td")
index_military_two = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td")
index_military_one = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td")

military = str("\n⚔Military Index\n\n" +
               "10 --> " + index_military_ten.get_text() + "\n" +
               "9 --> " + index_military_nine.get_text() + "\n" +
               "8 --> " + index_military_eight.get_text() + "\n" +
               "7 --> " + index_military_seven.get_text() + "\n" +
               "6 --> " + index_military_six.get_text() + "\n" +
               "5 --> " + index_military_five.get_text() + "\n" +
               "4 --> " + index_military_four.get_text() + "\n" +
               "3 --> " + index_military_three.get_text() + "\n" +
               "2 --> " + index_military_two.get_text() + "\n" +
               "1 --> " + index_military_one.get_text() + "\n\n By @Denver02"
               )



#### Config Induc
index_education_ten = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
        "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
        "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
        "td").findNext("td").findNext("td").findNext("td").findNext("td")
index_education_nine = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td")
index_education_eight = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td")
index_education_seven = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td")
index_education_six = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td")
index_education_five = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td")
index_education_four = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td")
index_education_three = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td")
index_education_two = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td")
index_education_one = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td")

education = str("\n📕Education Index\n\n" +
                "10 --> " + index_education_ten.get_text() + "\n" +
                "9 --> " + index_education_nine.get_text() + "\n" +
                "8 --> " + index_education_eight.get_text() + "\n" +
                "7 --> " + index_education_seven.get_text() + "\n" +
                "6 --> " + index_education_six.get_text() + "\n" +
                "5 --> " + index_education_five.get_text() + "\n" +
                "4 --> " + index_education_four.get_text() + "\n" +
                "3 --> " + index_education_three.get_text() + "\n" +
                "2 --> " + index_education_two.get_text() + "\n" +
                "1 --> " + index_education_one.get_text() + "\n\n By @Denver02"
                )


## dev config
index_development_ten = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
        "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
        "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
        "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
        "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td")
index_development_nine = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
        "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
        "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
        "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
        "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
        "td").findNext("td")
index_development_eight = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td")
index_development_seven = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td")
index_development_six = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td")
index_development_five = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td")
index_development_four = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td")
index_development_three = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td")
index_development_two = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td")
index_development_one = contenuto.find("th").findNext("th").findNext("th").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext("td").findNext(
    "td").findNext("td").findNext("td")

development = str("\n🏢Development Index\n\n" +
                  "10 --> " + index_development_ten.get_text() + "\n" +
                  "9 --> " + index_development_nine.get_text() + "\n" +
                  "8 --> " + index_development_eight.get_text() + "\n" +
                  "7 --> " + index_development_seven.get_text() + "\n" +
                  "6 --> " + index_development_six.get_text() + "\n" +
                  "5 --> " + index_development_five.get_text() + "\n" +
                  "4 --> " + index_development_four.get_text() + "\n" +
                  "3 --> " + index_development_three.get_text() + "\n" +
                  "2 --> " + index_development_two.get_text() + "\n" +
                  "1 --> " + index_development_one.get_text() + "\n\n By @Denver02"
                  )
