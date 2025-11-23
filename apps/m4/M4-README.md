# Milestone-4

## Technical Brief: Extending Beautiful Soup by Making it an Iterable Object
**Author:** *Nick Hlousek*

### Problem Definition
The Beautiful Soup Library creates a tree structure from an HTML/XML Object. Most operations
regarding the tree ineveitably end up searching the tree in some manner. The library already
has various methods to search the tree explicitly but it would be nice if we could just iterate
over the tree using a for loop to do our desired operations without any addtional method calls.

Essentially I think it would be helpful to add some semantic sugar in the form of an iterator/generator
to handle searching the tree.

### Implementation
The tag class, which the BeautifulSoup object inherits from, already has methods/attributes wich do a lazy breadth
first search on the both itself and the descendands of the node, thus to add the desired feature we simply need to
add an \_\_iter\_\_ method to BeautifulSoup which invokes this functionality. Additionally, keeping in the lazy mindset we
should also just yield the resutls to avoid extra memory storage.
