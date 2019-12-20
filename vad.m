%Program for removing silence from speech signal
clc
close all;
clear all;

signal_with_silence = audioread('7.wav');
subplot(2,1,1)
plot(signal_with_silence);
xlabel('Frequency (in Hz.)');
ylabel('Amplitude (in volts)');
title('Speech Signal with Silence');
grid on;
%Assigning values for creating frames
fs=16000;
frame_duration=0.01;
frame_len = frame_duration*fs;
N=length(signal_with_silence);
num_frames=floor(N/frame_len);
new_sig=zeros(N,1);
count=0;
%Creating Frames using for loop
for k = 1 : num_frames
    frame = signal_with_silence((k-1)*frame_len+1 : frame_len*k);
    max_val = max(frame);
    
    if (max_val>0.03)
        count = count + 1;
        new_sig((count-1)*frame_len+1 : frame_len*count) = frame;
    end
end
%Removing the ending zeros from signal without silence
signal_without_silence=new_sig(new_sig~=0);
%Plotting signal without silence
subplot(2,1,2)
plot(signal_without_silence);
xlabel('Frequency (in Hz.)');
ylabel('Amplitude (in volts)');
title('Speech Signal without Silence');
grid on;
%Separating two audio files with empty array
q=zeros(20000,1);
%Displaying the length of audio
disp('Length of Signal with Silence: ');
disp(length(signal_with_silence));
disp('Length of Signal without Silence: ');
disp(length(signal_without_silence));
%Playing both the audio files
combined = [signal_with_silence;q;signal_without_silence];
sound(signal_without_silence)
