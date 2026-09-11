import random, math
random.seed(1046)
# exact arithmetic
print("0.20*16^-1/4 =", 0.20*(16**-0.25))
print("0.70*16^-1/4 =", 0.70*(16**-0.25))
print("OSSS factor 2ln3 =", 2*math.log(3), " x0.20 =", 0.20*2*math.log(3))
# discretized proxy: 16x16 bits, left-right red crossing; interface exploration:
# random start row U in 0..15 on left edge; DFS red/blue boundary trace.
# Simplified revealment proxy: explore percolation interface via BFS of boundary.
# We estimate: mean query count and max-cell query frequency, plus crossing curve.
import collections
def has_lr_crossing(grid,n):
    # red=1 BFS from left column reds
    vis=set()
    from collections import deque
    q=deque()
    for r in range(n):
        if grid[r][0]==1:
            q.append((r,0)); vis.add((r,0))
    while q:
        r,c=q.popleft()
        if c==n-1: return True
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr,nc=r+dr,c+dc
            if 0<=nr<n and 0<=nc<n and (nr,nc) not in vis and grid[nr][nc]==1:
                vis.add((nr,nc)); q.append((nr,nc))
    return False

def interface_query_set(grid,n,U):
    # vertical-interface exploration: trace the red/blue interface starting at left-edge row U.
    # Model: walk the dual edges keeping red on left; reveal primal cells adjacent to walk.
    # Simplified certifiable proxy: BFS the connected 'boundary layer' from seed cell (U,0):
    # reveal all cells connected to seed via steps that stay on color-change edges.
    # Implement as: reveal cluster boundary of the monochrome component containing seed:
    # reveal component of seed color + its 4-neighbourhood. This determines crossing locally.
    from collections import deque
    queried=set()
    seedcol=grid[U][0]
    q=deque([(U,0)]); seen={(U,0)}
    while q:
        r,c=q.popleft()
        queried.add((r,c))
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr,nc=r+dr,c+dc
            if 0<=nr<n and 0<=nc<n and (nr,nc) not in seen and grid[nr][nc]==seedcol:
                seen.add((nr,nc)); q.append((nr,nc))
    # also reveal boundary neighbours (to know where component stops)
    extra=set()
    for (r,c) in list(seen):
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr,nc=r+dr,c+dc
            if 0<=nr<n and 0<=nc<n:
                extra.add((nr,nc))
    return queried|extra

def estimate(n, trials, p):
    cross=0; qcount=[0]*(n*n)
    for t in range(trials):
        grid=[[1 if random.random()<p else 0 for _ in range(n)] for __ in range(n)]
        if has_lr_crossing(grid,n): cross+=1
        U=random.randrange(n)
        qs=interface_query_set(grid,n,U)
        for (r,c) in qs: qcount[r*n+c]+=1
    return cross/trials, [x/trials for x in qcount]

for p in (0.25,0.5,0.75):
    cr,qf=estimate(16,2000,p)
    print(f"p={p} cross~{cr:.3f} maxReveal~{max(qf):.3f} meanQ~{sum(qf):.1f} cells")
