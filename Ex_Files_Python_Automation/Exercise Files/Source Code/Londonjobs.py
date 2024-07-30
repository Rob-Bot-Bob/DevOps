import csv
fileName = r"C:\Users\ferna\OneDrive\Documents\2024-07-10_-_Worker_and_Temporary_Worker.csv"
# f = open(fileName,'r')
# output1 = "Nearcecy.txt"
# output2 = "Noasnearofcecy.txt"
# passFile = open(output1,'w')
# failFile = open(output2, 'w')
cityList = [ "London", "LONDON", "Richmons", "Putney", "Hunslow", "Wimbledon", "Wembly" ] 

# reader_obj = csv.reader(f) 
      
#     # Iterate over each row in the csv  
#     # file using reader object 
# for row in reader_obj: 
#     if cityList in row:
#         print(row)  

def filter_lines(input_file, output_file, words):
    with open(input_file, 'r') as f_input, open(output_file, 'w') as f_output:
        for line in f_input:
            if any(word in line for word in words):
                f_output.write(line)

# Example usage:
if __name__ == "__main__":
    input_file = fileName  # Replace with your input file
    output_file = "Nearcecy.txt"  # Replace with your output file
    specific_words = cityList  # Array of specific words

    filter_lines(input_file, output_file, specific_words)
    print(f"Lines containing specific words have been filtered and saved to '{output_file}'.")

