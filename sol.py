import sys
import numpy as np



in_file = "b.txt"
out = ""
with open("data/" + in_file, 'r') as f:
        D, I, S, V, F = tuple(map(int, f.readline().split(" ")))
        street_to_idx = {}
        idx_to_street = [[""]*I for i in range(I)]

        duration = np.zeros(shape=(I, I))

        for _ in range(S):
            B, E, name, L = f.readline().split(" ")
            B, E, L = int(B), int(E), int(L)
            street_to_idx[name] = (B, E)
            idx_to_street[B][E] = name
            duration[B,E] = L

        total_flow = np.zeros(shape=(I, I))
        start_flow = np.zeros(shape=(I, I))

        for v in range(V):
            streets = f.readline().split()
            nb_streets = streets[0]
            del streets[0]

            B, E = street_to_idx[streets[0]]
            start_flow[B,E] = 1

            for street in streets:
                B,E = street_to_idx[street]
                total_flow[B,E] += 1

        
        out = str(I) + "\n"
        for i in range(I):
            best_starts = np.argsort(start_flow[:,i])
            best_starts = np.flip(best_starts)

            
            times = total_flow[:,i]
            out += str(i) + "\n" + str(np.count_nonzero(times)) + "\n"
            for b in best_starts:
                if times[b] == 0:
                    continue
                street_name = idx_to_street[b][i]
                out += street_name + " " + str(int(times[b])) + "\n"


        print(out)

out_file = in_file + ".out"
with open("/mnt/c/Users/gusta/Downloads/" + out_file, "w") as text_file:
    text_file.write(out)
                
            
            
            


