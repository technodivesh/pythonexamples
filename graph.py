# Implementing Graph in python

# example
graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }


class Graph:

    def __init__(self,graph={}):
        self.__graph = graph


    def vertices(self):
        return list(self.__graph.keys())

    def edges(self):

        edges = []
        for vertex in self.__graph:
            for ver in self.__graph[vertex]:
                edges.append((vertex,ver))
        return edges

    def add_vertex(self,vertex):

        if vertex not in self.__graph:
            self.__graph[vertex] = []

    def add_edge(self,edge):

        vertex1, vertex2 = tuple(edge)
        if vertex1 in self.__graph:
            self.__graph[vertex1].append(vertex2)

        else:
            self.__graph[vertex1] = [vertex2]

    def __repr__(self):
        _str = "Vertices: "
        _str += str(self.vertices())
        _str += "\nEdges: "
        _str += str(self.edges())

        return _str

    # def find_path(self, start_vertex, end_vertex, path=None):
    #     """ find a path from start_vertex to end_vertex 
    #         in graph """
    #     if path == None:
    #         path = []
    #     graph = self.__graph
    #     path = path + [start_vertex]
    #     if start_vertex == end_vertex:
    #         return path
    #     if start_vertex not in graph:
    #         return None
    #     for vertex in graph[start_vertex]:
    #         if vertex not in path:
    #             extended_path = self.find_path(vertex,end_vertex,path)
    #             if extended_path: 
    #                 return extended_path
    #     return None

    def find_path(self,start_vertex,end_vertex,path=None):
        """ find a path from start_vertex to end_vertex in graph """
        
        if path == None:
            path = []

        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path

        if end_vertex not in self.__graph:
            return None

        for vertex in self.__graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,end_vertex,path)

                if extended_path:
                    return extended_path

        return None


    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to 
            end_vertex in graph """
        graph = self.__graph
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,end_vertex,path)
                for p in extended_paths: 
                    paths.append(p)
        return paths


graph1 = Graph(graph)


