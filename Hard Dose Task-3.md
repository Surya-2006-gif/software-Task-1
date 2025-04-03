# HARD DOSE TASK -3

Below is my attached link for the behaviou tree

 ![root(--) (1)](https://github.com/user-attachments/assets/c4563d65-c485-4d12-9083-91c3a6c27173)


### How does the Fallback Node help in making better decisions?
            
   
    - I can think of few points why is the Fallback node better,it decision making behaviour can be made in a way of human decisions for example since the executuion goes from left to right if we keep important decisions on the left side the important decisions can be executed.Also it doesnt get struck if one of its child node doesnt tick,it goes for successsive child give rise to a more robust model

    -it handles the unexpected behaviour effectively,for example suppose a robot got blocked in its path way.The root node ticks with certain frequency right so if it has two nodes to handle the presence of obstacles and overcoming the obstacle it can handle any obstacles that comes in fron of it


### Why is this better than using long if-else conditions?

    -  the first thing is the readability ,the collection of fallback nodes are much more readable than the nested if-else statements

    - Next suppose i want to add a extra condition to handle a external agent we need to reconstruct the entire if else statements rather in this behavioural tree we just need to add a node



 ### What happens if the battery is low but not critically low? How does your tree handle this?

  -My  tree first checks if the battery is normal or not,it is not ticked so checks whether is it low since the condition is true it executes the leaf node which is turning off non essential systems                                    
