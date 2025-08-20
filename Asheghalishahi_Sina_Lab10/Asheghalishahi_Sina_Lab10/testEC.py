# Function that checks if a given matrix is a zero-matrix (all values 0)
def is_zero_matrix(func_matrix):
    for i in range(len(func_matrix)):
        for j in range(len(func_matrix[i])):
            if func_matrix[i][j] != 0:
                return False
    return True

# Main function
def main():
    # Get size of the matrix
    size = int(input("Enter size n of matrix for an n x n matrix: "))

    # Get matrix rows according to size and fill matrix
    matrix = []
    for i in range(size):
        row = input(f"Enter row {i+1} of zero-one adjacency matrix ({size} values with spaces in between): ")
        row_list = row.split()
        row_list = [int(x) for x in row_list]
        matrix.append(row_list)

    # Start the circuit with vertex 'a'
    circuit = ['a']
    previous = 'a'
    new = ''

    # Find the initial arbitrary circuit from vertex 'a' and remove the edges from the adjacency matrix
    while True:
        found_edge = False
        for i in range(size):
            for j in range(size):
                if chr(i + 97) == previous and matrix[i][j] == 1:
                    # Add vertex to the circuit
                    new = chr(j + 97)
                    circuit.append(new)
                    # Remove the edge
                    matrix[i][j] = 0
                    matrix[j][i] = 0
                    previous = new
                    found_edge = True
                    break
            if found_edge:
                break
        #break if back to initial vertex
        if previous == 'a' and found_edge:
            break

    # Find subcircuits that remain while edges still exist and add subcircuits into the circuit correctly
    while not is_zero_matrix(matrix):
        subcircuit = []
        previous = ''
        new = ''
        
        # Find an edge to start subcircuit with
        for i in range(size):
            for j in range(size):
                if matrix[i][j] == 1 and chr(i + 97) in circuit:
                    subcircuit.append(chr(i + 97))
                    previous = chr(i + 97)
                    break
            if subcircuit:
                break

        # Construct subcircuit
        while previous != new:
            if new != '':
                previous = new
            found_edge = False
            for i in range(size):
                for j in range(size):
                    if chr(i + 97) == previous and matrix[i][j] == 1:
                        # Add vertex to subcircuit
                        new = chr(j + 97)
                        subcircuit.append(new)
                        # Remove the edge
                        matrix[i][j] = 0
                        matrix[j][i] = 0
                        found_edge = True
                        break
                if found_edge:
                    break

        # Add subcircuit into the circuit
        index = circuit.index(subcircuit[0])
        circuit = circuit[:index + 1] + subcircuit[1:]

    #make sure circuit got back to initial vertex
    if circuit[-1] != 'a':
        circuit.append('a')

    # Print out the resulting Euler circuit
    print('\nEuler circuit: ')
    print(', '.join(circuit))

# Run main
main()
