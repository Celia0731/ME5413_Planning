import matplotlib.pyplot as plt
import rosbag
import os

bag = rosbag.Bag('/home/celia/ME5413/homework3/Planning_Project/src/me5413_world/error_my_robot.bag')

topics = [
    "/me5413_world/planning/abs_heading_error",
    "/me5413_world/planning/abs_position_error",
    "/me5413_world/planning/abs_speed_error",
    "/me5413_world/planning/rms_heading_error",
    "/me5413_world/planning/rms_position_error",
    "/me5413_world/planning/rms_speed_error",
]

filenames = ['error_analysis_abs.png', 'error_analysis_rms.png']

for i in range(2):
    plt.figure(figsize=(10, 15))
    for j in range(3):
        topic = topics[i * 3 + j]
        messages = bag.read_messages(topics=[topic])

        times = []
        errors = []
        for _, msg, t in messages:
            times.append(t.to_sec())
            errors.append(msg.data)

        plt.subplot(3, 1, j + 1)
        plt.plot(times, errors, label=topic.split('/')[-1])
        plt.title(topic.split('/')[-1])
        plt.xlabel("Time (s)")
        plt.ylabel("Error")
        plt.legend()

    plt.tight_layout()
    
    save_path = os.path.join('/home/celia/ME5413/homework3/Planning_Project/src/me5413_world/results/my_robot', filenames[i]) 
    plt.savefig(save_path)
    
    plt.show()

bag.close()
