base_url = "https://codefirstgirls.com"
category_urls = {
    "courses": "/courses",
    "opportunities": "/opportunities"
}
sub_category_urls = {
    "cfgdegree": "/courses/cfgdegree",
    "ambassadors": "/opportunities/ambassadors"
}

current_url = base_url

while True:
    print(f"You are currently on the URL {current_url}")

    if current_url == base_url:
        print("Where are you clicking?\nOptions: Courses, Opportunities")
    elif current_url == base_url + category_urls["courses"]:
        print("Where are you clicking?\nOptions: CFGDegree, Back")
    elif current_url == base_url + sub_category_urls["cfgdegree"]:
        print("Where are you clicking?\nOptions: Back")
    elif current_url == base_url + category_urls["opportunities"]:
        print("Where are you clicking?\nOptions: Ambassadors, Back")
    elif current_url == base_url + sub_category_urls["ambassadors"]:
        print("Where are you clicking?\nOptions: Back")

    choice = input().lower()

    if choice == "back":
        if current_url == base_url:
            break
        elif current_url == base_url + sub_category_urls["cfgdegree"]:
            current_url = base_url + category_urls["courses"]
        else:
            current_url = base_url
    elif choice in category_urls.keys():
        current_url = base_url + category_urls[choice]
    elif choice in sub_category_urls.keys():
        current_url = base_url + sub_category_urls[choice]


# Space and Time Complexity:
# Both the time and space complexity of the provided code are O(1) due to the fixed and constant nature of the
# operations and memory usage.

# Time Complexity:
#
# The time complexity of the code depends on the number of iterations in the while loop.
# When the user chooses an option other than "Back": The code performs a constant-time lookup to determine the new URL
# based on the user's choice. This operation has a time complexity of O(1).
#
# When the user chooses "Back": There are multiple branches for different URL cases (if and elif statements).
# Each branch involves comparisons and assignments, which are all constant-time operations (O(1)).
# The number of times these operations are performed depends on the nested conditions.
# Since the number of iterations and operations within each iteration is relatively small and constant, we can consider
# the overall time complexity of the code to be O(1).
#
# Space Complexity:
#
# Variables: The variables used in the code (base_url, category_urls, sub_category_urls, current_url, and choice)
# occupy a constant amount of memory regardless of the input size. Therefore, the space used by variables is O(1).
#
# Data Structures: The data structures used in the code are dictionaries (category_urls and sub_category_urls) to store
# URL mappings. The size of these dictionaries is fixed and does not change based on the input size. As a result, the
# space used by the dictionaries is O(1).
# Considering that the memory usage remains constant regardless of the input, we can conclude that the space complexity
# of the code is O(1).
#
# Assumptions:
# The number of categories and sub-categories is fixed and does not change during runtime.
# The user's input is assumed to be valid and follows the expected format ("Courses", "Opportunities", "Back", etc.).
