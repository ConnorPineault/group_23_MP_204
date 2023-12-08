# CISC/CMPE 204 Modelling Project

Group 23's Modelling Project.

Brief Explaination: 

1 - This project models a slightly simplified version of standard poker. 
2 - This version includes 3 given (dealt) cards, and 2 cards that act as shared table cards (the river).
3 - The model determines the rank of each players hand, and uses the ranks to determine the winner.
4 - The model provides suggestions to the player on if the player should play, or fold the hand.
5 - The model also features a model accuracy function, which can determine the accuracy of the models predications over large sample sizes.

A more in depth description, break down, and analysis of the model can be found in the project report. 

                                    GROUP_23_MP_204 > final > project_report

To explore the model, run the program through the run.py file.

                                    GROUP_23_MP_204 > run.py

Related Jape proofs both solved and explained can be found at

                                    GROUP_23_MP_204 > final > JapeExplanation OR proofs.jp







## Running With Docker

By far the most reliable way to get things running is with [Docker](https://www.docker.com). This section runs through the steps and extra tips to running with Docker. You can remove this section for your final submission, and replace it with a section on how to run your project.

1. First, download Docker https://www.docker.com/get-started

2. Navigate to your project folder on the command line.

3. We first have to build the course image. To do so use the command:
`docker build -t cisc204 .`

4. Now that we have the image we can run the image as a container by using the command: `docker run -it -v $(pwd):/PROJECT cisc204 /bin/bash`

    `$(pwd)` will be the current path to the folder and will link to the container

    `/PROJECT` is the folder in the container that will be tied to your local directory

5. From there the two folders should be connected, everything you do in one automatically updates in the other. For the project you will write the code in your local directory and then run it through the docker command line. A quick test to see if they're working is to create a file in the folder on your computer then use the terminal to see if it also shows up in the docker container.

### Mac Users w/ M1 Chips

If you happen to be building and running things on a Mac with an M1 chip, then you will likely need to add the following parameter to both the build and run scripts:

```
--platform linux/x86_64
```

For example, the build command would become:

```
docker build --platform linux/x86_64 -t cisc204 .
```

### Mount on Different OS'

In the run script above, the `-v $(pwd):/PROJECT` is used to mount the current directory to the container. If you are using a different OS, you may need to change this to the following:

- Windows PowerShell: `-v ${PWD}:/PROJECT`
- Windows CMD: `-v %cd%:/PROJECT`
- Mac: `-v $(pwd):/PROJECT`

Finally, if you are in a folder with a bunch of spaces in the absolute path, then it will break things unless you "quote" the current directory like this (e.g., on Windows CMD):

```
docker run -it -v "%cd%":/PROJECT cisc204
```
