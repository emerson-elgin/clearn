from sensors import read_dht, read_analog
from mqtt_client import publish_to_cloud
from edge_prediction import predict_environment

# Main Loop
def main():
    while True:
        try:
            # Read sensor data
            temp, humidity = read_dht()
            rain = read_analog("rain_sensor")
            mq6 = read_analog("mq6_sensor")
            
            # Edge AI Prediction
            prediction = predict_environment([temp, humidity, rain, mq6])

            # Publish data to cloud
            publish_to_cloud(temp, humidity, rain, mq6, prediction)
            print(f"Published: Temp={temp}, Humidity={humidity}, Rain={rain}, MQ6={mq6}, Prediction={prediction}")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
