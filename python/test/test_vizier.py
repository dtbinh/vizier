import asyncio
import mqtt_interface.mqttInterface as mqttInterface
import functools as ft
import time
import json
import argparse
import queue
import vizier.vizier as vizier

def main():

    parser = argparse.ArgumentParser()
    #TODO: Add support for separate experiments
    #parser.add_argument("experimend_id", type=int, help="The ID of the experiment")
    parser.add_argument("config", help=".json file node information")
    parser.add_argument("-port", type=int, help="MQTT Port", default=8080)
    parser.add_argument("-host", help="MQTT Host IP", default="localhost")

    args = parser.parse_args()

    print(args)

    #Ensure that we can open the nodes file

    config = None
    try:
        f = open(args.config, 'r')
        config = json.load(f)
        f.close()
    except Exception as e:
        print(repr(e))
        print("Couldn't open given node file " + args.config)
        return -1


    # TODO: DON'T FORGET TO UNSUBSCRIBE FROM CHANNELS
    setup_channel = 'vizier/setup'
    node_descriptors = config["nodes"]

    vizier.construct(args.host, args.port, setup_channel, *node_descriptors)

if(__name__ == "__main__"):
    main()
