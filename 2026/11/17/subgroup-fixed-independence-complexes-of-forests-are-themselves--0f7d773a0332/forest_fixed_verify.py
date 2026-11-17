"""Independent finite checks for forest-independence fixed-space classification.

Python 3, NetworkX. Reproduces the tests without external files.
"""
import itertools
import networkx as nx


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def generated_group(n, generators):
    ident = tuple(range(n))
    group = {ident}
    stack = [ident]
    while stack:
        g = stack.pop()
        for h in generators:
            z = compose(g, h)
            if z not in group:
                group.add(z)
                stack.append(z)
    return sorted(group)


def quotient_model(graph, group):
    unseen = set(graph.nodes())
    orbits = []
    while unseen:
        start = min(unseen)
        orbit = tuple(sorted({g[start] for g in group}))
        orbits.append(orbit)
        unseen.difference_update(orbit)
    eligible = [o for o in orbits if all(not graph.has_edge(a,b) for a,b in itertools.combinations(o,2))]
    q = nx.Graph()
    q.add_nodes_from(range(len(eligible)))
    for i, j in itertools.combinations(range(len(eligible)), 2):
        if any(graph.has_edge(a,b) for a in eligible[i] for b in eligible[j]):
            q.add_edge(i,j)
    return q, eligible, orbits


def sphere_or_point(graph):
    graph = graph.copy()
    dimension = -1  # the empty realization is recorded as the formal sphere S^{-1}
    while graph.number_of_nodes():
        if any(degree == 0 for _, degree in graph.degree()):
            return None
        leaf = next(v for v,d in graph.degree() if d == 1)
        center = next(iter(graph.neighbors(leaf)))
        graph.remove_nodes_from(set(graph.neighbors(center)) | {center})
        dimension += 1
    return dimension


def faces_from_graph(graph):
    nodes = list(sorted(graph.nodes()))
    out = []
    for k in range(len(nodes)+1):
        for comb in itertools.combinations(nodes,k):
            if all(not graph.has_edge(u,v) for u,v in itertools.combinations(comb,2)):
                out.append(comb)
    return out


def boundary_rank(face_list, k):
    if k < 0: return 0
    higher = [x for x in face_list if len(x) == k+1]
    lower = [x for x in face_list if len(x) == k]
    positions = {x:i for i,x in enumerate(lower)}
    pivots = {}
    for face in higher:
        vec = 0
        for j in range(len(face)):
            sub = face[:j]+face[j+1:]
            vec ^= 1 << positions[sub]
        while vec:
            pivot = vec.bit_length()-1
            if pivot in pivots: vec ^= pivots[pivot]
            else:
                pivots[pivot] = vec
                break
    return len(pivots)


def betti_mod2(face_list):
    # Reduced complex includes the empty face as a (-1)-cell.
    max_size = max(map(len,face_list))
    dims = [sum(len(f)==k for f in face_list) for k in range(max_size+1)]
    ranks = [0] + [boundary_rank(face_list,k-1) for k in range(1,max_size+1)]+[0]
    # ranks[k+1] is rank of boundary from k-faces to (k-1)-faces.
    return [dims[k]-ranks[k]-ranks[k+1] for k in range(max_size+1)]


def reduced_lefschetz(graph, permutation):
    total = -1  # augmented empty simplex
    for face in faces_from_graph(graph):
        if not face: continue
        mapped = [permutation[v] for v in face]
        if set(mapped) != set(face): continue
        inverted = sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
        total += (-1)**(len(face)-1+inverted)
    return total


def validate(graph, group):
    model,eligible,orbits = quotient_model(graph,group)
    assert model.number_of_nodes()==0 or nx.is_forest(model)
    fixed_faces = []
    for face in faces_from_graph(graph):
        f=set(face)
        if all({g[v] for v in f} == f for g in group):
            fixed_faces.append(tuple(i for i,o in enumerate(eligible) if set(o).issubset(f)))
    model_faces=faces_from_graph(model)
    assert len(fixed_faces)==len(model_faces) and set(fixed_faces)==set(model_faces)
    kind=sphere_or_point(model)
    hom=betti_mod2(model_faces)
    expected=[0]*len(hom)
    if kind is not None: expected[kind+1]=1
    assert hom==expected, (graph.edges(),kind,hom,expected)
    base=sphere_or_point(graph)
    if len(group)==1 or all(compose(g,h) in group for g in group for h in group):
        for g in group:
            lefschetz=reduced_lefschetz(graph,g)
            if base is None:
                assert lefschetz==0
            else:
                assert abs(lefschetz)==1
                # A cyclic generator's fixed locus has the same Lefschetz number.
                cyclic_model,_,_=quotient_model(graph,generated_group(len(graph),[g]))
                degree=sphere_or_point(cyclic_model)
                assert degree is not None
                assert lefschetz==(-1)**(degree)
                assert lefschetz // ((-1)**base) == (-1)**(degree-base)
    return len(model_faces)


def case_tree_tests():
    cases=0
    faces=0
    for n in range(2,9):
        for tree in nx.nonisomorphic_trees(n):
            tree = nx.convert_node_labels_to_integers(tree)
            a=list(nx.algorithms.isomorphism.GraphMatcher(tree,tree).isomorphisms_iter())
            if len(a)>48:continue
            for perm in a:
                group=generated_group(n,[tuple(perm[i] for i in range(n))])
                faces+=validate(tree,group)
                cases+=1
    return cases,faces


def case_noncyclic_tests():
    cases=0
    faces=0
    # Three-arm spider: the rooted branch permutation group is S3.
    spider=nx.Graph()
    spider.add_edges_from((0,1+i) for i in range(3))
    spider.add_edges_from((1+i,4+i) for i in range(3))
    n=7
    for generators in [
        [(0,2,1,3,5,4,6),(0,2,3,1,5,6,4)],
        [(0,2,3,1,5,6,4)],
        [(0,2,1,3,5,4,6)],
    ]:
        group=generated_group(n,generators)
        faces+=validate(spider,group)
        cases+=1
    # Four disjoint edges with cyclic, double-transposition and S4 actions.
    graph=nx.Graph()
    graph.add_edges_from((2*i,2*i+1) for i in range(4))
    def permute_edges(p):return tuple(2*p[i//2]+i%2 for i in range(8))
    swap=permute_edges((1,0,2,3))
    cycle=permute_edges((1,2,3,0))
    flip=tuple(i^1 for i in range(8))
    for generators in [[swap,cycle],[cycle],[swap,flip],[flip]]:
        group=generated_group(8,generators)
        faces+=validate(graph,group)
        cases+=1
    return cases,faces

if __name__=='__main__':
    a,b=case_tree_tests()
    c,d=case_noncyclic_tests()
    print('tree automorphism cyclic-subgroup instances:',a)
    print('noncyclic/generated subgroup instances:',c)
    print('fixed orbit faces compared:',b+d)
    print('FOREST_INDEPENDENCE_FIXED_MODELS_PASS')
