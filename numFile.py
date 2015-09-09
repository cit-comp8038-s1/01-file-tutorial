__author__ = 'larkin cunningham'

infile = open("DataNums.txt", 'r')
rainfall = [eval(line) for line in infile]
infile.close()

print("Average rainfall was {0:.2f} mm.".format(sum(rainfall) / len(rainfall)))