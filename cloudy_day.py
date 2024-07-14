def maximumPeople(p, x, y, r):
    events = {}
    n = len(p)
    m = len(y)
    
    for i in range(n):
        if x[i] in events:
            events[x[i]].append((2, p[i]))
        else:
            events[x[i]] = [(2, p[i])]
    
    for i in range(m):
        if y[i] - r[i] in events:
            events[y[i] - r[i]].append((1, i + 1))
        else:
            events[y[i] - r[i]] = [(1, i + 1)]
        
        if y[i] + r[i] + 1 in events:
            events[y[i] + r[i] + 1].append((-1, i + 1))
        else:
            events[y[i] + r[i] + 1] = [(-1, i + 1)]
    
    not_under_attack = 0
    active = set()
    bomber_pop = [0] * (m + 1)
    
    
    for cord in sorted(events.keys()):
        v = events[cord]
        v.sort()
        
        for event in v:
            if event[0] == -1:
                active.discard(event[1])
            elif event[0] == 1:
                active.add(event[1])
            else:
                if len(active) == 1:
                    bomber_pop[list(active)[0]] += event[1]
                elif len(active) == 0:
                    not_under_attack += event[1]
    
    mx = max(bomber_pop)
    return not_under_attack + mx

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    p = list(map(int, data[1:n+1]))
    x = list(map(int, data[n+1:2*n+1]))
    
    m = int(data[2*n+1])
    y = list(map(int, data[2*n+2:2*n+2+m]))
    r = list(map(int, data[2*n+2+m:]))
    
    result = maximumPeople(p, x, y, r)
    print(result)
