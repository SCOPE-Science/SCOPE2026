"""Check that the cyclic LCF and Fano-incidence encodings coincide."""
fano_edges = {tuple(sorted(((i+d) % 7, 7+i))) for i in range(7) for d in (0,1,3)}
lcf_edges = {tuple(sorted((i, (i+1) % 14))) for i in range(14)}
lcf_edges |= {tuple(sorted((i, (i+5) % 14))) for i in range(0,14,2)}
# Vertex i of LCF corresponds to the point/line vertex mapping[i].
mapping = (0,7,3,9,2,13,6,10,4,8,1,12,5,11)
mapped_edges = {tuple(sorted((mapping[a],mapping[b]))) for a,b in lcf_edges}
assert len(fano_edges) == len(lcf_edges) == 21
assert sorted(mapping) == list(range(14))
assert mapped_edges == fano_edges
print('graph_isomorphism_passed')
