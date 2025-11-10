# Milestone-3

## Technical Brief: Extending Beautiful Soup with SoupReplacer
**Author:** *Nick Hlousek*

### Problem Definition
One of the main use cases of the Beautiful Soup library is to parse an html/xml file structure,
find a subset of tags inside that structure, and then modify said tags in some manner.  

As stated, there is some inefficiences in this process. Namely that after Beautiful Soup generates the tree structure, it then has to parse the structure to find the tags that need modification. Thus not only is the user paying the cost to generate the structure and modify it, they are also paying the cost to find the tag that they need to modify for every modification they are going to do.  

However if we know what modifcations we want to make before we create the tree stucture we should in theory be able to do the modifications while creating the tree thus removing the extra time that would be spent searching through the tree and improve the performance of the library for this general use case.  

### Implementation Options
Both options which I will list below involve the creation of an object called a **SoupReplacer**. This object will encapsulate the modifcations to the tree that the user would like to do and will be used by the BeautifulSoup object during the creation of the tree to make the necessary modigications. My intention is for this object to be passed into the constructor of the BeautifulSoup object as an optional argument and some modifications will need to be made to the BeautifulSoup object for it to use the SoupReplacer appropriately.  

The difference in implementation corresponds to what information do we want the SoupReplacer object to store in order for the replacements to take place during the parsing phase.

#### Data Approach
One way we can do this is to directly store the data that needs to be modified. The replacer object will contain the name of the tag that needs to be replaced and a list of modifications that need to be made to said tag.

The structure of the object would be a list of pairs of new tags and old tags. This could be extended to attributes and the like but for ease I have implemnted a simplified version in release v2 that only considers one pair of name tags, but this could be easliy extended in later versions to acocunt for more than one match.

The primary benefit of this approach is that it is very straightforward to use. The user need simply define the replacements to make and the SoupReplacer object will take care of the rest.

#### Functional Approach
While the simplicity layed out in the above approach is nice, we could make a slight modification to what is stored to give much more general behavior at the cost of some additional complexity demanded from the user.

Instead of storing the data that needs to be modified, if we instead store the operation we allow the user to have alot more control over the replacements they would want to make.

The additional complexity comes from the fact that we will need the user to define the operation they would like to take place as a function that they would pass into the SoupReplacer constructor.

### Suggested Approach
Looking at the two approaches I've suggested, I believe we should move forward with the funcional approach
as there is no functionality that us lost by doing this and it could make more complex transformations simpler to do for the user.
