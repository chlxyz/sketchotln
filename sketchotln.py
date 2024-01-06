import cv2

set_input = "" # Specify the input file
set_output = "" # Specify the output file

def sketchotln(frame, sigma_s=60, sigma_r=0.07):
    # Apply stylization filter for an sketch outline effect
    outline = cv2.stylization(frame, sigma_s=sigma_s, sigma_r=sigma_r)

    return outline

def process_video(input_video_path, output_video_path):
    cap = cv2.VideoCapture(input_video_path)
    width = int(cap.get(3))
    height = int(cap.get(4))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Apply the sketch outline effect
        applied_frame = sketchotln(frame)

        # Write the frame to the output video
        out.write(applied_frame)

        # Display the result (optional)
        cv2.imshow("Result", applied_frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_video_path = set_input
    output_video_path = set_output

    process_video(input_video_path, output_video_path)
