def seconds_to_minutes(seconds):
    minutes = seconds / 60
    return round(minutes,1)

def main():
    filename = "trips.csv"
    infile = open(filename)
    header = infile.readline()
    durations = []
    for line in infile: 
        line = line.removesuffix("\n")
        row =line.split(",")
        trip = int(row[0])
        durations.append(trip)

    print("The number of trips is", len(durations))
    print('The average trip duration is', sum(durations)/len(durations))
    print("The longest trip duration is", max(durations))
    print("The shortest trip duration is", min(durations))
    n = len(durations)
    index_a = (n-1)//2
    index_b = (n)//2
    print("The median trip duration is", (sorted(durations)[index_a] + sorted(durations)[index_b]) / 2)

if __name__ == "__main__":
    main()







    
    
