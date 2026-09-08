# Consolidated verification script: rebuilds all claimed numbers from scratch (stdlib only).
from cover import check_cover, dfs_cover_exists, build_masks, pop
# Claim 1: reciprocal census values (exact integer arithmetic)
N=2520
U=[2,3,4,5,6,7,8,9,10,12,14,15,18,20,21,24,28,30]
divs=sorted(d for d in range(1,N+1) if N%d==0)
assert len(divs)==48
elig4_full=[m for m in U if m>=4]
assert elig4_full==[4,5,6,7,8,9,10,12,14,15,18,20,21,24,28,30]
assert sum(N//m for m in elig4_full)==3984, sum(N//m for m in elig4_full)
ok_count=sum(1 for L in divs if sum(L//m for m in [x for x in elig4_full if L%x==0])>=L)
assert ok_count==8, ok_count
oks=sorted(L for L in divs if sum(L//m for m in [x for x in elig4_full if L%x==0])>=L)
assert oks==[120,180,360,420,504,840,1260,2520], oks
print('reciprocal census OK:', oks)
# Claim 2: max-coverage witness density 2422/2520
wit=[(4,3),(5,0),(6,2),(7,0),(8,1),(9,0),(10,2),(12,1),(14,2),(15,1),(18,6),(20,4),(21,3),(24,5),(28,6),(30,28)]
cov,bad=check_cover(wit,2520)
assert cov==2422 and len(bad)==98, (cov,len(bad))
print('witness density OK: 2422/2520, uncovered 98')
# Claim 3: UNSAT L=120 and L=180 full eligible sets
for L,elig in [(120,[4,5,6,8,10,12,15,20,24,30]),(180,[4,5,6,9,10,12,15,18,20,30])]:
    out,wit2,nodes,dt=dfs_cover_exists(elig,L,node_cap=20000000,time_cap=300)
    assert out=='UNSAT',(L,out)
    print(f'UNSAT OK L={L} nodes={nodes}')
print('ALL FINAL CHECKS PASSED')
