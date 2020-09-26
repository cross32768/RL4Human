import argparse
import gym


def main():
    parser = argparse.ArgumentParser(
        description="Script to play OpenAI-gym for human")
    parser.add_argument("--env", type=str, default="CartPole-v0")
    args = parser.parse_args()

    try:
        from msvcrt import getch
    except ImportError:
        def getch():
            import sys
            import tty
            import termios
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                return sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)

    env = gym.make(args.env)
    assert isinstance(env.action_space,
                      gym.spaces.Discrete), "Action shoule be discrete"
    assert env.action_space.n < 10, "Too many action"
    print("Action Space:", env.action_space)
    try:
        print(env.get_action_meanings())
    except:
        pass

    env.reset()
    env.render()
    done = False
    while not done:
        key = ord(getch())
        action = key - ord("0")
        assert 0 <= action and action < env.action_space.n, "Invalid Action"
        _, _, done, _ = env.step(key - ord("0"))
        env.render()
        if done:
            env.close()

if __name__ == "__main__":
    main()
