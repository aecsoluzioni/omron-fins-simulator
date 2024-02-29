FROM ruby:3.0
RUN useradd -m omron
USER omron
WORKDIR /home/omron
COPY omron_plc.rb omron_plc.rb
ENTRYPOINT [ "ruby", "omron_plc.rb" ]