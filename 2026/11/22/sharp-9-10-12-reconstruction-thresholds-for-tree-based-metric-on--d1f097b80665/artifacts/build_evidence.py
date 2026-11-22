from verify import tree_families, stats, species_poly, occupancy_coefficients, adjacency
import json, pathlib
p=pathlib.Path(__file__).parent
fams=tree_families(12)
rows=['n\tunlabelled_trees\tscalar_collision_fibres\toccupancy_collision_fibres\tdistance_graded_collision_fibres\tmax_fibre_scalar\tmax_fibre_occupancy\tmax_fibre_distance_graded']
for n in range(1,13):
    vals=[]
    for mode in ('scalar','occupancy','species'):
        _,hits=stats(fams[n],mode)
        vals.append((len(hits),max(map(len,hits),default=1)))
    rows.append('\t'.join(map(str,[n,len(fams[n]),vals[0][0],vals[1][0],vals[2][0],vals[0][1],vals[1][1],vals[2][1]])))
(p/'census.tsv').write_text('\n'.join(rows)+'\n',encoding='utf-8')
data={}
for name,n in [('scalar',9),('occupancy',10),('species',12)]:
    _,hits=stats(fams[n],name)
    assert len(hits)==1 and len(hits[0])==2
    trees=[]
    for key,edges in hits[0]:
        poly=species_poly(n,edges)
        trees.append({'canonical_unrooted_AHU':key,'edges_zero_based':[list(e) for e in edges],
                      'degree_multiset':sorted(len(z) for z in adjacency(n,edges)),
                      'scalar_non_algebraic_one_type_count':sum(poly.values()),
                      'occupancy_coefficients_low_to_high':list(occupancy_coefficients(n,poly)),
                      'species_coefficients':[{"n_distance_1":a,"n_distance_3":b,"count":v}
                        for ((a,b),v) in sorted(poly.items())]})
    data[name]={'order':n,'collision_fibres':1,'fibre_size':2,'witnesses':trees}
(p/'witnesses.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print((p/'census.tsv').read_text())
