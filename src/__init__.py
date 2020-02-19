#!/usr/bin/env python3

from websites import fatabyyano as f
import sys

sys.path.append("websites")


def main():
    print("main")
    fatabyyano = f.FatabyyanoFactCheckingSiteExtractor()

    """ 
    retrieve_listing_page_urls = fatabyyano.retrieve_listing_page_urls()
    number_of_page = fatabyyano.find_page_count(fatabyyano.get(retrieve_listing_page_urls[0]))
    claims_url = fatabyyano.retrieve_urls(fatabyyano.get(retrieve_listing_page_urls[0]),retrieve_listing_page_urls[0],number_of_page) # takes 4 min
    for url in claims_url:
        print(url) 
    """

    for line in sys.stdin:
        line.rstrip()  # enleve le dernier '\n' de la ligne
        webpage = fatabyyano.get(line)
        tags = fatabyyano.extract_tags(webpage)
        date = fatabyyano.extract_date(webpage)
        claim = fatabyyano.extract_claim(webpage)
        rating = fatabyyano.extract_rating_value(webpage)
        if tags == [] or claim == "" or rating == "" or claim == "" or date == "":
            print(line)  # print url
        else:
            print(rating + " --> " +
                  f.FatabyyanoFactCheckingSiteExtractor.translate_rating_value(rating))
            print(tags)

        """
        print(claim)
        print(value)
        """


if __name__ == "__main__":
    main()
