import itertools, random
from engine import is_fano_free, bipartite_edge_set, b_n, min_edit_distance, H_unbalanced_internal

def report(n, H, name):
    bn=b_n(n)
    e=len(H)
    defect=bn-e
    ff, wit = is_fano_free(n,H)
    d, U = min_edit_distance(n,H)
    print(f"{name}: n={n} e={e} b={bn} defect={defect} defect/n^3={defect/n**3:.4f} dist={d} dist/n^3={d/n**3:.4f} ratio={('inf' if defect<=0 else f'{d/defect:.2f}')} fanofree={ff}")
    return ff, defect, d

# baseline unbalanced+internal variants at n=8,9
for n in [8,9]:
    bn=b_n(n)
    for nx in [5,6,7]:
        for internal in ['empty','bip','clique','star']:
            for nx1 in ([None] if internal!='bip' else [1,2,3]):
                if internal=='bip':
                    H=H_unbalanced_internal(n,nx,nx1,internal)
                    name=f"unbal nx={nx} bip nx1={nx1}"
                else:
                    H=H_unbalanced_internal(n,nx,None,internal)
                    name=f"unbal nx={nx} {internal}"
                report(n,H,name)
    print('---')
