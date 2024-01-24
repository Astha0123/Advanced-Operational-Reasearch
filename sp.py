#optimal_path=[]
def find_shortest_path(graph):
    n = len(graph)

    # Initialize the network
    f = [float('inf')] * n
    f[0] = 0

    # Keep track of optimal paths at each stage
    optimal_paths = [[] for _ in range(n)]
    optimal_paths[0] = [1]  # Start from the first city

    # Dynamic Programming Recursion
    for i in range(1, n):
        for j in range(i):
            # Assuming the graph represents distances between cities
            if f[j] + graph[j][i] < f[i]:
                f[i] = f[j] + graph[j][i]
                optimal_paths[i] = optimal_paths[j] + [i + 1]  # Adjust indexing
 
        # Print information at each stage
        # print(f"\nStage {i} - Optimal Distance: {f[:i + 1]}")
        # print(f"Optimal Paths: {optimal_paths[:i + 1]}")

    # Determine Overall Optimal Decision or Policy
    overall_optimal_distance = f[n - 1]
    overall_optimal_path = optimal_paths[n - 1]
    #print(optimal_paths)
    #print(f)
    return overall_optimal_distance, overall_optimal_path,optimal_paths,f

# Given Graph
graph = [
    [0, 7, 8, 9, float('inf'), float('inf'), float('inf')],  # Stage 1
    [float('inf'), 0, float('inf'), float('inf'), 12, float('inf'), float('inf')],  # Stage 2
    [float('inf'), float('inf'), 0, float('inf'), 8, 9, float('inf')],   # Stage 3
    [float('inf'), float('inf'), float('inf'), 0, 7, 13, float('inf')],  # Stage 4
    [float('inf'), float('inf'), float('inf'), float('inf'), 0, float('inf'), 9, ],   # Stage 5
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0, 6, ],   # Stage 6
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0]    # Stage 7
]

#for i in
#for i in range(len)

# Example Usage
result_distance, result_path,optimal_path,optimal_distance = find_shortest_path(graph)

#print(optimal_path)
#print(len(optimal_path))
max=1
for i in range(len(optimal_path)):
     if(len(optimal_path[i])>max):
       max=len(optimal_path[i])
     #print(len(optimal_path[i]))

l=len(optimal_path)
# print(max)
# print(optimal_distance)
for i in range(1,max+1):
   print(f"\nStage {i}:")
   for j in range(0,l):
      #print(len(optimal_path[j]))
        if(len(optimal_path[j])==i):
           print(f"\npath{optimal_path[j]}:---optimal_distance\t:{optimal_distance[j]}")

print(f"\nThe shortest path distance is: {result_distance}")
print(f"The overall optimal path is: {result_path}")