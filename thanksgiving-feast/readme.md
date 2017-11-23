# Printing Turkeys

## Link

https://codegolf.stackexchange.com/questions/148841/thanksgiving-feast

## My Solution

* Language(s): [Python]

My solution focused on finding how many white lovers or dark lovers there were. Figuring out the max here means that the other group is satisfied. However, that does not mean that the whole group is satisfied, so I figured out how many servings were remaining to figure out the actual total. I then implemented a fairly straight forward turkey printing solution

## Evaluation

* Performance: Unsubmitted

Turns out I don't need to do that complicated logic. If I get the bound on how many total servrings are required and compare that against the max of white/dark lovers, then this will give me the correct answer, saving a fair amount of bytes and simplifying the algorithm. Printing had some minor savings.
