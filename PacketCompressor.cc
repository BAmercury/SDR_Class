#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/if_ether.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <netinet/udp.h>
#include <netinet/tcp.h>
#include <arpa/inet.h>
#include <sys/time.h>

#include <functional>

#include "Logger.hh"
#include "net/PacketCompressor.hh"

using namespace std::placeholders;

PacketCompressor::PacketCompressor()
  : net_in(*this, nullptr, nullptr, std::bind(&PacketCompressor::netPush, this, _1))
  , net_out(*this, nullptr, nullptr)
  , radio_in(*this, nullptr, nullptr, std::bind(&PacketCompressor::radioPush, this, _1))
  , radio_out(*this, nullptr, nullptr)
{
}

void PacketCompressor::netPush(std::shared_ptr<NetPacket> &&pkt)
{
    // You will want to allocate sizeof(struct ether_header) *fewer* bytes here!
    buffer<unsigned char> buf(pkt->size());

    // Change this to copy from the packet into the buffer in two steps:
    //   1) Copy the extended header
    //   2) *Skip* the Ethernet header and copy the rest of the packet
    memcpy(buf.data(), pkt->data(), pkt->size());
    pkt->swap(buf);
    // Update the extended header with new size since we've removed the Ethernet
    // header
    // pkt->ehdr().data_len -= sizeof(struct ether_header);

    net_out.push(std::move(pkt));
}

void PacketCompressor::radioPush(std::shared_ptr<RadioPacket> &&pkt)
{
    // You'll want to add an additional sizeof(struct ether_header) bytes when
    // allocating the buffer.
    buffer<unsigned char> buf(pkt->size());
    
    // Construct the Ethernet header here. You'll need to figure out the proper
    // source and destination Ethernet addresses, which can be determined
    // completely from pkt->curhop and pkt->nexthop.
    /*
    ether_header ehdr = { { ... }
                        , { ... }
                        , htons(ETHERTYPE_IP)
                        };
    */

    // Change this to copy from the packet into the buffer in three steps:
    //   1) Copy the extended header
    //   2) Copy your constructed Ethernet header
    //   2) Copy the rest of the packet
    memcpy(buf.data(), pkt->data(), pkt->size());
    pkt->swap(buf);
    // Update the extended header with new size since we've added the Ethernet
    // header
    // pkt->ehdr().data_len += sizeof(struct ether_header);

    radio_out.push(std::move(pkt));
}
