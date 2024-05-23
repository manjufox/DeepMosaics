@REM python deepmosaic.py -ss 00:02:00 -t 00:03:00 --all_mosaic_area --mode clean --netG video --ex_mult 5 --fps 30 --mask_threshold 5 --media_path ./input/ --model_path ".\pretrained_models\mosaic\clean_youknow_video.pth" --gpu_id 0 
@REM python deepmosaic.py --no_preview --all_mosaic_area --mode clean --netG video --ex_mult 3 --fps 30 --mask_threshold 5 --media_path ./input/ --model_path ".\pretrained_models\mosaic\clean_youknow_video.pth" --gpu_id 0 
@REM python deepmosaic.py -ss 00:04:20 -t 00:04:30 --mode clean --netG video --fps 30 --mask_threshold 64 --media_path ./input/ --model_path ".\pretrained_models\mosaic\clean_youknow_video.pth" --gpu_id 0 
python deepmosaic.py --no_preview --mode clean --netG video --fps 30 --mask_threshold 64 --media_path ./input/ --model_path ".\pretrained_models\mosaic\clean_youknow_video.pth" --gpu_id 0 

