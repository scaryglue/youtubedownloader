from pytube import YouTube
import pathlib

def print_available_streams(stream, aorv):
    print('These are the available Streams: ')

    if aorv == 'a' or aorv == 'A':
        print(stream.filter(only_audio=True))
    else:
        print(stream.filter(file_extension='mp4'))


    user_input = input('Which of the following streams do you want to download? Please enter the correct itag and make sure it is contained in the stream.')

    while not user_input.isnumeric():
        print('Wrong Input! Put in a number that is contained in the stream.')
        user_input = input('Which of the following streams do you want to download? Please enter the correct itag and make sure it is contained in the stream.')

    return (int) (user_input)





def main():
    
    while True:
        link = input('Enter the YouTube Link of the video you want to download: ')

        video = YouTube(link)

        aorv = input('Do you want to download the video or the audio? [V/A]')

        while aorv != 'a' and aorv != 'A' and aorv != 'v' and aorv != 'V':
            aorv = input('Incorrect input! Please choose from the options [V/A]. \nDo you want to download the video or the audio? [V/A]')

        itag = print_available_streams(video.streams, aorv)

        stream = video.streams.get_by_itag(itag)

        stream.download()

        print('Video successfully downloaded!')



if __name__ == "__main__":
    main()



