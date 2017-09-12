# 538war
This is a quick and dirty little script to come up with a solution for: [a fivethrityeight puzzler](https://fivethirtyeight.com/features/riddler-nation-goes-to-war/).

I think the obvious solution to the quick puzzler is to just shift everything off by 1 so:

3 4 5 6 7 8 9 10 J Q K A 2

Which would rock it against one but not so much against the reverse order where the tie breaker goes in the house's favor. The simple solution there is to just swap the first and last cards so:

2 4 5 6 7 8 9 10 J Q K A 3

Though that would allow an entry I'd imagine that most people would do something along those lines, so to beat other people's entries we would need to do something a bit stronger.  

It is hard to know what other people will do.  One thought is that having 9 in the middle would beat both orderings where the 8 is in the middle, and so I'd imagine a lot of people would do that.  So we could swap that with the 10, and it might be a guaranteed win against most peoples hands.  

However if you want to modify a hand to be able to beat itself, swaps won't do anything you'd be swapping a win and a loss for a loss and a win.  You can though do a 3-way swap that might improve over the others.  

Under the assumption that most people will do as few swaps as possible from one of the starting arrangements, I tried getting as far as possible away.  As long a new arrangment was beats an old one I kept it.  Then kept going in a sort of simple genetic algorithm.  

In the end the arrangement is more or less random - which makes me think I could have come up with a different coding solution to get a random order a lot faster.  I'm not convinced I'll end up beating much more than 50% but at least I had a bit of fun throwing this together.



