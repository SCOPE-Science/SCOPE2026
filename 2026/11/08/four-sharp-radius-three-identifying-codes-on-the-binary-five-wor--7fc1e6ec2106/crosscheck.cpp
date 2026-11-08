// Independent directed-graph BFS census of five-bit identifying codes.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <queue>
#include <stdexcept>
#include <vector>

int main() {
    constexpr int n = 32;
    std::array<std::vector<int>, n> reverse_neighbors;
    for (int u = 0; u < n; ++u) {
        for (int bit = 0; bit <= 1; ++bit) {
            int v = ((u << 1) & 31) | bit;
            reverse_neighbors[v].push_back(u);
        }
    }
    std::array<uint32_t, n> balls{};
    for (int target = 0; target < n; ++target) {
        std::queue<std::pair<int,int>> bfs;
        std::array<bool,n> visited{};
        bfs.push({target,0});
        visited[target]=true;
        while(!bfs.empty()) {
            auto [u,dist]=bfs.front(); bfs.pop();
            balls[target] |= (uint32_t(1) << u);
            if (dist==3) continue;
            for(int pred: reverse_neighbors[u]) {
                if (!visited[pred]) {
                    visited[pred]=true;
                    bfs.push({pred,dist+1});
                }
            }
        }
    }
    std::vector<int> found;
    for (int f = 0; f < (1 << 16); ++f) {
        uint32_t code=0;
        for (int prefix=0; prefix<16; ++prefix) {
            int word = (prefix << 1) | ((f >> prefix) & 1);
            code |= (uint32_t(1) << word);
        }
        std::array<uint32_t,n> ids{};
        bool valid=true;
        for (int v=0; v<n; ++v) {
            ids[v] = balls[v] & code;
            if (ids[v] == 0) valid=false;
        }
        if (!valid) continue;
        std::sort(ids.begin(),ids.end());
        if (std::adjacent_find(ids.begin(),ids.end()) == ids.end()) {
            found.push_back(f);
        }
    }
    if (found != std::vector<int>({6949,6951,23333,23335})) {
        throw std::runtime_error("unexpected binary graph census");
    }
    std::cout << "CROSSCHECK_OK 4\n";
}
