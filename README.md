# Furbnow
[![Screenshot-2023-02-24-at-11-47-57.png](https://i.postimg.cc/5yRnNtz0/Screenshot-2023-02-24-at-11-47-57.png)](https://postimg.cc/SYcWgkDF)


## Running the Project
- `pip install -r rquirements.txt`
- `python manage.py runserver`
- Navigate to `/measures` on the browser

## Feature Recommendations
- Use a frontend framework such as React to set state so that the user can view the increase in costs in real-time as each item is clicked. Use Django Rest Framework to build the API to send data to the frontend framework
- Allow users to filter measures based on various criteria such as cost, energy savings, or environmental impact. This would provide users with a more personalized experience.
- Add a feature to show popular measures.
- Add a modal when a measure is clicked, that features images and additional information that would capture the user's imagination.

## Decisions
- Created a urls.py file for the app
- Added a checkbox input next to each measure to allow users to select measures.
- Included a form to collect measures selected by the user.
- Processed the form data submitted by the user to calculate the total cost using Django request.POST to get the values of the selected measures.
