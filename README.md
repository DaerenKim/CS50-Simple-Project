# CS50-Simple-Project

Title: Color-Coded Checklist Video Demo: https://youtu.be/fnhjKuocaFs?si=sRX_UK0IwADS-W-H

Description: I will be designing and implementing a dynamic checklist application aimed at enhancing task organization and prioritization. This application will allow users to input tasks along with their due dates. Once entered, tasks will be sorted automatically by the number of days left before the task is due, ensuring that the most urgent task is displayed at the top of the list. To further improve usability, the application will incorporate a color-coding system to visually represent the urgency of each task:

Red: Tasks due within the next 24 hours will be highlighted in red, signaling immediate attention. Overdue tasks will also be in red Yellow: Tasks due within the next 3 days will be marked in orange, indicating high priority. Green: Tasks due within a week will be displayed in yellow, showing moderate urgency. Blue: Tasks due in more than a week will appear in green, denoting low priority. The application will feature 4 primary functions: generate(), sort(), display_table() and check(), each designed to address a specific aspect of task management.

Function Breakdown:

main():

The main() function gives the users 4 choices to select from: For the 1st option (Add Task), it asks for the user's task and due date, then calls the generate() function For the 2nd option (Check Task), it calls the check() function, allowing users to check off their desired task For the 3rd option (View Checklist), it calls the display_table() function to let the users see the current task list For the 4th option (Exit), it exits the program

generate():

This function will serve as the entry point for users to add new tasks. After collection the user inputs in the main() function, it will call this function. This function serves to calculate the number of days between the due date and the current date. Based on the number of days, an urgency is assigned to the task, categorised by colours, as explained above. The function then appends each task and its due date, remaining days and urgency, as a dictionary, to the list named content. The function then calls the sort() and display_table() function

sort():

The sort() function will be automatically triggered whenever a new task is added. It will reorganize the checklist based on the chronological order of days remaining before the tasks are due. This ensures that tasks with the nearest deadlines always appear at the top, providing a clear focus on immediate priorities. The sort() function operates seamlessly in the background, maintaining a well-ordered checklist without requiring user intervention.

display_table():

check():

This function allows users to mark tasks as completed and remove them from the checklist. Users can specify which task to check off by entering a command in the terminal, such as "check1" to remove the first task on the list. Once a task is marked as completed, the checklist will automatically update to reflect the change. The check() function ensures that the checklist remains clean and focused, displaying only active tasks. The dynamic nature of this application means that every user interaction will immediately reflect in the checklist. Whether adding, sorting, or checking tasks, the application will present users with a real-time, visually intuitive, and structured overview of their responsibilities.
