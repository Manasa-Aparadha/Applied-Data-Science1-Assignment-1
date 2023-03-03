#Code for LINE GRAPH
#Import libraries
import pandas as pd
import matplotlib.pyplot as plt

#Define a function to visualize crime data from a CSV file
def visualize_crime_data(data_file):
    
    # Read the data from CSV file
    df = pd.read_csv(data_file)

    # Select the first 11 states for visualization
    states = df["STATE"][:11]
    murder = df["Murder"][:11]
    rape = df["Rape"][:11]
    robbery = df["Robbery"][:11]

    # Create a figure of appropriate size
    plt.figure(figsize = (10,5))

    # Plot the data for murder, rape, and robbery for the selected states
    plt.plot(states, murder, label = "Murder")
    plt.plot(states, rape, label = "Rape")
    plt.plot(states, robbery, label = "Robbery")

    # Set x-axis and y-axis labels and legend
    plt.xlabel("STATE")
    plt.ylabel("NUMBER OF CRIMES")
    plt.title("Crimes in Indian States 2019")
    plt.legend()

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation = 90)

    # Show the plot
    plt.show()

# Call the function and provide the data file path as input
visualize_crime_data("crimes.CSV")


#Code for BAR GRAPH

#Define a function to plot the number of Super Bowl wins by state
def plot_superbowl_wins(file_path, states):
    
    # Read the CSV file into a DataFrame df
    df = pd.read_csv(file_path)

    # Group the data by state and count the number of wins
    team_wins = df.groupby('State').size().reset_index(name = 'Wins')

    # Select only the specified states from the CSV file for the X-axis
    team_wins = team_wins[team_wins['State'].isin(states)]

    # Create the bar plot
    plt.bar(team_wins['State'], team_wins['Wins'])

    # Set the axis labels and title
    plt.xlabel('State')
    plt.ylabel('Number of Wins')
    plt.title('Super Bowl Wins by State')

    # Create a legend
    plt.legend(['Number of Wins'], loc = 'upper right')

    # Show the plot
    plt.show()

# Call the function with the file path and list of states
file_path = ("superbowl.CSV")
states = ['California', 'Texas', 'Florida', 'Louisiana', 'Michigan', 'Georgia']
plot_superbowl_wins(file_path, states)


#Code for PIE Chart

##Define a function to chart the Total Tips by day of the week
def get_total_tips_by_day(filename):
    data = pd.read_csv(filename)
    total_tips = data.groupby('day')['tip'].sum()
    return total_tips

# Call the function to get the total tips by day of the week
total_tips = get_total_tips_by_day("tips.CSV")

# Create a pie chart of the total tips by day of the week
plt.pie(total_tips,
        labels = total_tips.index,
        autopct = '%1.1f%%',
        shadow = True)

#Set title and legend
plt.title('Total Tips by Day of the Week')
plt.legend(title = 'Day', loc = 'best')
plt.axis('equal')
plt.show()
