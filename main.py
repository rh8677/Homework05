import csv
import matplotlib.pyplot as plt
import pandas
import seaborn
import sys


def agglomeration():
    return


# This function will read in the csv file specified in the command line (if the file is valid),
# and provides hints to the user if there is anything wrong with the command line arguments.
if __name__ == '__main__':
    # If the amount of arguments (plus the name of the program) is not 2, we will inform the user.
    if len(sys.argv) != 2:
        print("Error - invalid number of arguments (must specify the csv file)")
    else:
        try:
            # The second cmd argument is the csv file we have to open and retrieve data from
            with open(sys.argv[1]) as csv_file:
                read_data = csv.reader(csv_file)
                headers = next(read_data)[1:]  # A list of the names of the item groups (excluding ID)
                number_col = len(headers)  # Find the amount of item groups there are
                item_lists = [[]] * number_col  # An array of the frequencies for each item group

                # For each row of data we append individual values to its corresponding group column
                for row in read_data:
                    item_counter = 0

                    # We want to skip over the IDs
                    for row_item in row[1:]:
                        frequency = int(row_item.strip())

                        # If the array is empty, we initialize one with the value to append included
                        if not item_lists[item_counter]:
                            item_lists[item_counter] = [frequency]
                        else:
                            item_lists[item_counter].append(frequency)
                        item_counter += 1

                dictionary_data = dict(zip(headers, zip(*item_lists)))  # Converts item_lists to a dictionary
                data_frame = pandas.DataFrame(dictionary_data, columns=headers)  # Convert the dictionary to data frame
                correlation_matrix = data_frame.corr()  # We get a cross-correlation coefficient matrix
                seaborn.heatmap(correlation_matrix, annot=True)  # We map the matrix on a heatmap
                plt.show()  # Show the matrix in a new window

            csv_file.close()

            # If the file is unable to be opened for whatever reason, we will inform the user.
        except OSError:
            print("Error - cannot open file '" + sys.argv[1] + "'")
