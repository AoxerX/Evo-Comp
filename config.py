"""
Initialisation Settings
"""

# Plotting
save_world_view = True
fig_size = 20  # pixel size is fig_size x dpi
check_newly_spawned = True

save_world_view = True

world = dict(
    settings=dict(
        seed='rt0_t0-cs_L-001',
        rows=100,
        columns=100,
        fertile_lands=[[[20, 20], [79, 79]]],
        init_food=500,
        init_bugs=100
    ),
    food_spawn_vals=dict(
        energy=20,
        reproduction_threshold=25,
        energy_max=100
        # TODO: food & bug taste
    ),
    bug_spawn_vals=dict(
        energy=20,
        reproduction_threshold=60,
        energy_max=100
    )
)

food_endangered_threshold = 100
bug_endangered_threshold = 50

food_over_shadow = True
food_over_shadow_ratio = 0.5

food = dict(
    growth_rate=2,

    # Evolution switches
    evolve_reproduction_threshold=False,
    reproduction_threshold_mutation_limit=5,

    evolve_taste=False,
    taste_mutation_limit=10
)

bug = dict(
    respiration_rate=3,
    eat_tax=1,

    # Evolution switches
    evolve_reproduction_threshold=False,
    reproduction_threshold_mutation_limit=5,

    evolve_taste=False,
    taste_mutation_limit=10
)
