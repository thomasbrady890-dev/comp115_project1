# Project: "Cows Playing Hockey"
**Developer:** Tom 
**Lead Designers:** Emilia (Age 4) and Avery (Age 2)

---

## Concept & Inspiration

For this Python Turtle assignment, I decided to compensate for my lack of creativity by consulting with a "Creative Focus Group" — my daughters, Emilia and Avery. 

Through our brainstorming session, they provided a very specific set of stakeholder requirements for this scene:
1. A bright sun and a colorful rainbow are mandatory.
2. High mountains and a green meadow.
3. Cows playing hockey. 

The result is "Cows Playing Hockey," where the competitive spirit of hockey meets a serene, mountain-side meadow.

---

## Technical Details

To make my daughters' vision come to life, I used several Python concepts we learned in class:

* **Modular Functions:** I created a unique function for every object—draw_cow, draw_ice_rink, draw_rainbow, etc. This kept the code organized and allowed me to fix the sun without accidentally breaking the hockey rink.
* **The "Size" Variable:** To create depth, I used a "size" parameter in the cow function. This allowed me to draw a huge crowd of 250 small cows in the background while keeping the two main players large and in the foreground.
* **Procedural Randomization:** I used the "random" library to place the clouds and the spectator cows. This means every time the girls watch the program run, the crowd stands in different spots!
* **Optimization:** Because drawing 250 cows is a lot of work for a computer and takes a long time, I used the `tracer` command. This draws everything in the background first so the final scene appears instantly for the user. This was very helpful with debugging, as it meant I didn't have to wait for the turtle to finish before realizing that my cows' heads were detached from their bodies.

---

## How to Run

1. Open the `hockey_cows.py` file in VS Code.
2. Click the "Play" button in the top right corner.
3. Wait a moment for the scene to load.
4. **To Exit:** Simply click anywhere on the drawing window to close it.