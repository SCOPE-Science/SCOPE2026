"""Chordless-cycle enumerator (for even-hole tests on larger graphs) + famous-graph screen.

For each candidate famous graph: n, even-hole-free?, omega, chi (exact when feasible),
and whether it violates chi <= max(3, ceil(3w/2)).
"""
import itertools, sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1499/output/artifacts')
from tools import from_edges, max_clique_size, chromatic_number, greedy_upper
import networkx as nx


def chordless_holes(masks, n, cap_even=1, cap_total=200):
    """Enumerate chordless cycles length>=4 via DFS from min vertex. Returns (even_holes, total)."""
    even = []
    total = [0]
    for s in range(n):
        if len(even) >= cap_even and total[0] >= cap_total:
            break
        Ns = masks[s]
        # neighbors of s greater than s start paths
        def dfs(path, used):
            if len(even) >= cap_even and total[0] >= cap_total:
                return True
            cur = path[-1]
            nb = masks[cur] & ~used
            # only vertices > s
            m = nb
            while m:
                lsb = m & (-m); m ^= lsb
                w = lsb.bit_length() - 1
                if w < s:
                    continue
                aws = (masks[w] >> s) & 1
                if aws:
                    if len(path) >= 3:
                        # check w nonadjacent to path[1..-2] (w neighbours cur=path[-1] by construction)
                        bad = False
                        for u in path[1:-1]:
                            if (masks[w] >> u) & 1:
                                bad = True; break
                        if not bad:
                            total[0] += 1
                            if (len(path) + 1) % 2 == 0:
                                even.append(tuple(path) + (w,))
                                if len(even) >= cap_even and total[0] >= cap_total:
                                    return True
                    # else triangle-ish, ignore
                else:
                    # extend if w nonadjacent to path[:-1]
                    bad = False
                    for u in path[:-1]:
                        if (masks[w] >> u) & 1:
                            bad = True; break
                    if not bad:
                        if dfs(path + [w], used | (1 << w)):
                            return True
            return False
        for v in range(s + 1, n):
            if (Ns >> v) & 1:
                dfs([s, v], (1 << s) | (1 << v))
    return even, total[0]


def nx_to_masks(G):
    G = nx.convert_node_labels_to_integers(G)
    n = G.number_of_nodes()
    m = [0] * n
    for i, j in G.edges():
        m[i] |= (1 << j); m[j] |= (1 << i)
    return m, n


def mycielski(k):
    G = nx.Graph(); G.add_edge(0, 1)  # M2 = K2
    # M_{k}: iterate mycielskian from M2 up to Mk
    for _ in range(k - 2):
        G = nx.mycielskian(G)
    return G


def build_candidates():
    C = {}
    C['C5'] = nx.cycle_graph(5)
    C['C7'] = nx.cycle_graph(7)
    C['petersen'] = nx.petersen_graph()
    C['chvatal'] = nx.chvatal_graph()
    C['desargues'] = nx.desargues_graph()
    C['M3=C5'] = mycielski(3)
    C['M4=grotzsch'] = mycielski(4)
    C['M5'] = mycielski(5)
    C['oddwheel7'] = nx.wheel_graph(8)  # C7 + hub, w=3
    C['Gr_3x3'] = nx.grid_2d_graph(3, 3)
    C['kneser6-2'] = nx.kneser_graph(6, 2)
    C['kneser7-2'] = nx.kneser_graph(7, 2)
    C['circulant9-13'] = nx.circulant_graph(9, [1, 3])
    C['circulant11-123'] = nx.circulant_graph(11, [1, 2, 3])
    C['moebius8'] = nx.moebius_kantor_graph()
    return C


def main():
    out_lines = []
    for name, G in build_candidates().items():
        masks, n = nx_to_masks(G)
        even, total = chordless_holes(masks, n, cap_even=2, cap_total=500)
        ehf = (len(even) == 0)
        w = max_clique_size(masks, n) if n <= 24 else -1
        if n <= 16:
            chi = chromatic_number(masks, n)
        else:
            chi = greedy_upper(masks, n)
            chi = "lo<=%d" % chi
        bound = max(3, -(-3 * w // 2)) if w > 0 else '?'
        line = "%-16s n=%-3d EHF=%-5s omega=%s chi=%s bound=%s" % (name, n, ehf, w, chi, bound)
        print(line, flush=True)
        out_lines.append(line)
    with open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1499/output/artifacts/screen_out.txt', 'w') as f:
        f.write("\n".join(out_lines) + "\n")


if __name__ == '__main__':
    main()
