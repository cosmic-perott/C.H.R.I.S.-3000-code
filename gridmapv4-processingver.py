ArrayList<Circle> circles;
int[][] clusterCenters = {
  {30, 30},
  {70, 70},
  {60, 60},
  {20, 80}
};
int numPoints = 200;
int clickRadius = 4;

void setup() {
  size(700, 800);
  circles = new ArrayList<Circle>();
  background(255);
  drawGrid();
  drawTower();

  for (int i = 0; i < numPoints; i++) {
    int[] center = clusterCenters[int(random(clusterCenters.length))];
    float x = constrain((float)(randomGaussian() * 5 + center[0]), 10, 100);
    float y = constrain((float)(randomGaussian() * 5 + center[1]), 10, 100);

    float sx = map(x, 0, 100, 0, width);
    float sy = map(y, 0, 100, height, 0);

    growOrCreateCircle(sx, sy);
  }

  noLoop();
}

void draw() {
  for (Circle c : circles) {
    c.display();
  }
}

void drawGrid() {
  stroke(220);
  strokeWeight(1);
  for (int i = 0; i <= 100; i += 5) {
    float x = map(i, 0, 100, 0, width);
    float y = map(i, 0, 100, height, 0);
    line(x, 0, x, height);
    line(0, y, width, y);
  }
}

void drawTower() {
  float centerX = width / 2;
  float centerY = height / 2;
  float towerRadius = 30;

  fill(0);
  noStroke();
  ellipse(centerX, centerY, towerRadius * 2, towerRadius * 2);

  fill(255);
  textAlign(CENTER, CENTER);
  textSize(18);
  text("tower", centerX, centerY);
}

void growOrCreateCircle(float x, float y) {
  for (Circle c : circles) {
    float d = dist(c.x, c.y, x, y);
    if (d < clickRadius * (width / 100.0)) {
      c.radius += 1;
      c.updateColor();
      return;
    }
  }
  Circle newC = new Circle(x, y, 1);
  circles.add(newC);
}

class Circle {
  float x, y;
  float radius;
  color c;

  Circle(float x_, float y_, float r_) {
    x = x_;
    y = y_;
    radius = r_;
    updateColor();
  }

  void updateColor() {
    if (radius <= 2) {
      c = color(0, 0, 255, 90); // Blue
    } else if (radius <= 5) {
      c = color(0, 200, 0, 90); // Green
    } else if (radius <= 8) {
      c = color(255, 255, 0, 90); // Yellow
    } else {
      c = color(255, 0, 0, 90); // Red
    }
  }

  void display() {
    noStroke();
    fill(c);
    float pxRadius = radius * (width / 100.0);
    ellipse(x, y, pxRadius * 2, pxRadius * 2);

    // Display radius value as text inside the circle
    fill(255);
    textAlign(CENTER, CENTER);
    textSize(10 + radius); // Slight scaling with radius
    text(int(radius), x, y);
  }
}
