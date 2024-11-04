from rdflib import Graph
import sys

def ttl_to_mermaid(ttl_file, mermaid_file):
    # Load the TTL file
    g = Graph()
    g.parse(ttl_file, format='turtle')

    # Prepare the Mermaid output
    mermaid_output = ["graph TD;"]
    node_mapping = {}

    # Function to get a unique node ID
    def get_node_id(uri):
        if uri not in node_mapping:
            node_mapping[uri] = f"node{len(node_mapping) + 1}"
        return node_mapping[uri]

    for s, p, o in g:
        subject_id = get_node_id(str(s))
        object_id = get_node_id(str(o))

        # Add the relationship
        if "hasChild" in str(p):
            mermaid_output.append(f"    {subject_id}[{s.split('/')[-1]}] --> {object_id}[{o.split('/')[-1]}];")

    # Write to the Mermaid file
    with open(mermaid_file, 'w') as f:
        f.write("\n".join(mermaid_output))

if __name__ == "__main__":
	ttl_file = 'your_rdf_file.ttl'
	mermaid_file = 'test.mmd'

	ttl_to_mermaid(ttl_file, mermaid_file)
	print(f"Converted {ttl_file} to {mermaid_file}")
