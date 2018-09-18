# Problem statement:
Consider the small town of Randomville, where people are crazy about their two sports
teams, the Randomville Reds and the Randomville Blues. The Reds had been around for a
long time, and people loved them. But then some out-of-town millionaire came along and
bought the Reds' top scorer and started a new team, the Blues. To the discontent of most
Reds fans, the top scorer would go on to win the championship title with the Blues. Years
later he would return to the Reds, despite some backlash from fans who could never forgive
him for his earlier career choices. But anyway, you can see why fans of the Reds don't
necessarily get along with fans of the Blues. In fact, these two fan bases are so divided that
they never even live next to each other. I've even heard stories where the Red fans
deliberately moved away once Blues fans moved in next door. True story!
Anyway, we are new in town and are trying to sell some Blues merchandise to people by
going from door to door. However, every now and then we come across a bleeding-heart
Reds fan who yells at us for selling Blues stuff and chases us off their lawn. Not nice! It
would be much less stressful, and a better use of our time, to avoid these houses altogether
and just visit the Blues fans instead.
Confident that we can learn to predict where the Reds fans live, we start keeping track of
our encounters. If we come by a Reds fan's house, we draw a red triangle on we handy
town map; otherwise, we draw a blue square. After a while, we get a pretty good idea of
where everyone lives:

![randomtownmap](https://user-images.githubusercontent.com/25251763/45686094-21555200-bb69-11e8-9376-11a798d9a2a7.png)

However, now we approach the house that is marked as a green circle in the preceding
map. Should we knock on their door? We try to find some clue as to what team they prefer
(perhaps a team flag hanging from the back porch), but we can't see any. How can we know
if it is safe to knock on their door?

## Solution :
As we mentioned earlier, fans of the Reds are really passionate about their team, so they
would never move next to a Blues fan. Couldn't we use this information and look at all the
neighboring houses, in order to find out what kind of fan lives in the new house?
This is exactly what the k-NN algorithm would do.
