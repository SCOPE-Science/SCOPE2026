// Exhaustive geodesic-mask verification for C3 Cartesian C8 (24 labelled vertices).
// Independent of the Cartesian-interleaving Python implementation.
// Compile: c++ -std=c++17 -O2 verify_torus_bfs.cpp -o torus_bfs
// Run: ./torus_bfs
#include <array>
#include <cstdint>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
using U = uint32_t;
constexpr int W = 8, N = 3 * W;
array<vector<int>, N> adj;
array<array<int, N>, N> distance_graph;
array<array<vector<U>, N>, N> paths;
array<uint64_t, N + 1> feasible{}, maximal{};
constexpr U full = (U(1) << N) - 1;

void enumerate_shortest_paths(int start, int destination, int vertex, U interior) {
    if (vertex == destination) {
        paths[start][destination].push_back(interior);
        return;
    }
    for (int next : adj[vertex]) {
        if (distance_graph[next][destination] + 1 ==
            distance_graph[vertex][destination]) {
            U added = interior | (vertex == start ? 0 : (U(1) << vertex));
            enumerate_shortest_paths(start, destination, next, added);
        }
    }
}

bool mutual_visible(U selection) {
    U first = selection;
    while (first) {
        int a = __builtin_ctz(first);
        first &= first - 1;
        U second = first;
        while (second) {
            int b = __builtin_ctz(second);
            second &= second - 1;
            bool clear = false;
            for (U interior : paths[a][b]) {
                if (!(interior & selection)) { clear = true; break; }
            }
            if (!clear) return false;
        }
    }
    return true;
}

void traverse(U selection, int first_allowed, int count) {
    ++feasible[count];
    bool is_maximal = true;
    U outside = full ^ selection;
    while (outside) {
        int v = __builtin_ctz(outside);
        outside &= outside - 1;
        if (mutual_visible(selection | (U(1) << v))) {
            is_maximal = false;
            break;
        }
    }
    if (is_maximal) ++maximal[count];
    for (int v = first_allowed; v < N; ++v) {
        U candidate = selection | (U(1) << v);
        if (mutual_visible(candidate)) traverse(candidate, v + 1, count + 1);
    }
}

int main() {
    for (int column = 0; column < W; ++column) {
        for (int row = 0; row < 3; ++row) {
            int u = 3 * column + row;
            for (int other = 0; other < 3; ++other)
                if (row != other) adj[u].push_back(3 * column + other);
            adj[u].push_back(3 * ((column + 1) % W) + row);
            adj[u].push_back(3 * ((column + W - 1) % W) + row);
        }
    }
    for (int a = 0; a < N; ++a) {
        distance_graph[a].fill(N + 1);
        distance_graph[a][a] = 0;
        queue<int> q;
        q.push(a);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : adj[u]) {
                if (distance_graph[a][v] > distance_graph[a][u] + 1) {
                    distance_graph[a][v] = distance_graph[a][u] + 1;
                    q.push(v);
                }
            }
        }
    }
    for (int a = 0; a < N; ++a)
        for (int b = a + 1; b < N; ++b)
            enumerate_shortest_paths(a, b, a, 0);
    for (int a = 0; a < N; ++a)
        for (int b = a + 1; b < N; ++b)
            if (paths[a][b].empty()) return 2;
    traverse(0, 0, 0);
    uint64_t total_feasible = 0, total_maximal = 0;
    for (int k = 0; k <= N; ++k) {
        if (feasible[k]) cout << k << ' ' << feasible[k] << ' ' << maximal[k] << '\n';
        total_feasible += feasible[k];
        total_maximal += maximal[k];
    }
    cout << "total_feasible " << total_feasible << '\n';
    cout << "total_maximal " << total_maximal << '\n';
    return 0;
}
