#!/usr/bin/env python3
import click
import xml.etree.ElementTree as ET

@click.command()
@click.argument('filename', type=click.File('rb'))
def depth(filename):
    """Max depth of xml (FILENAME)."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
    except Exception as e:
        click.echo(('File: %s is not xml.' %filename)+ ' Error: '+str(e))
        return False
    d=0
    if len(root)>0:
        list_tree=[root]
    else:
        list_tree=[]
    def dell_depth(root):
        elements_with_child=[]
        for tree in root:    
            for i in range(len(tree)):
                if len(tree[i])>0:
                    elements_with_child.append(tree[i])
        return elements_with_child
    while len(list_tree)>0:
        d+=1
        list_tree=dell_depth(list_tree)
    # click.echo('Depth = %d' %d)
    print('Depth = %d' %d)

if __name__ == '__main__':
    depth()




