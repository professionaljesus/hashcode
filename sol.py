import sys
import numpy as np
from tqdm import tqdm



in_files = list("bcdef")

for ff in in_files:
    in_file = ff + ".txt"
    out = ""
    print("for in_file " + in_file)
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
        
        num_cars = 0
        for v in range(V):
            streets = f.readline().split()
            nb_streets = streets[0]
            del streets[0]
        
            tot_tuples = []
            tot_L = 0
        
            for street in streets:
                B,E = street_to_idx[street]
                tot_tuples.append((B,E))
                tot_L += duration[B,E]
        
            if tot_L > float(D):
                continue
                
            num_cars += 1
            B, E = street_to_idx[streets[0]]
            start_flow[B,E] = 1
            for tup in tot_tuples:
                total_flow[tup[0],tup[1]] += 1
        
        print(V,num_cars)
        
        num_I = 0
        for i in tqdm(range(I)):
           # total_flow[:,i] = np.power(total_flow[:,i],2)
            if np.sum(total_flow[:,i]) > 0:
                norm = total_flow[:,i]/np.sum(total_flow[:,i])
            else:
                norm = total_flow[:,i]
        
            norm *= 3.1*np.count_nonzero(total_flow[:,i])
        
            best_starts = np.argsort(start_flow[:,i])
        
            best_starts = np.flip(best_starts)
            
            #times = (total_flow[:,i])
            times = np.ceil(norm)
            
            if np.count_nonzero(times) == 0:
                continue 

            out += str(i) + "\n" + str(np.count_nonzero(times)) + "\n"
            for b in best_starts:
                if times[b] == 0:
                    continue
                street_name = idx_to_street[b][i]
                out += street_name + " " + str(int(times[b])) + "\n"
            num_I += 1
        
        
        out = str(num_I) + "\n" + out
        print(out)
    
    out_file = in_file + ".out"
    with open("/mnt/c/Users/gusta/Downloads/" + out_file, "w") as text_file:
        text_file.write(out)
                    
                
                
            


