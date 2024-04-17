from vpython import *
import random


# Function to create a random initial position for particles
def random_position(radius):    
    theta = 2 * pi * random.random()
    phi = acos(2 * random.random() - 1)
    x = radius * sin(phi) * cos(theta)
    y = radius * sin(phi) * sin(theta)
    z = radius * cos(phi)
    return vector(x, y, z)


# Function to create a random velocity vector
def random_velocity(max_speed):
    vx = random.uniform(-max_speed, max_speed)
    vy = random.uniform(-max_speed, max_speed)
    vz = random.uniform(-max_speed, max_speed)
    return vector(vx, vy, vz)


# Create the scene
scene = canvas(title='Black Hole Simulation')

# Create the black hole
black_hole = sphere(pos=vector(0, 0, 0), radius=1, color=color.orange)

# Parameters
num_particles = 1000
initial_radius = 50  # Initial radius for particle distribution
absorption_radius = black_hole.radius * 2  # Radius at which particles get absorbed
particle_radius = 0.25
particle_color = color.white
time_step = 0.1
gravitational_constant = 1  # Simplified gravitational constant
black_hole_mass = 1000  # Simplified mass of the black hole
max_initial_speed = 1  # Maximum initial speed for particles

# Generate particles
particles = []
for _ in range(num_particles):
    particle_pos = random_position(initial_radius)
    particle = sphere(pos=particle_pos, radius=particle_radius, color=particle_color)
    particle.velocity = random_velocity(max_initial_speed)  # Random initial velocity
    particles.append(particle)

# Animation loop
while True:
    rate(100)
    for particle in particles:
        # Calculate distance to black hole
        distance = mag(particle.pos - black_hole.pos)
        if distance < absorption_radius:
            # Remove particle if it's too close to the black hole
            particle.visible = False
            particles.remove(particle)
            continue

        # Gravitational force calculation
        force_magnitude = gravitational_constant * black_hole_mass / distance ** 2
        force_direction = norm(black_hole.pos - particle.pos)
        force = force_direction * force_magnitude

        # Update particle velocity and position
        particle.velocity += force * time_step
        particle.pos += particle.velocity * time_step
