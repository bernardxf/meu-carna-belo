class BlocoEvent {
  final String id;
  final String name;
  final DateTime dateTime;
  final String description;
  final String address;
  final String neighborhood;
  final String? ticketPrice;
  final String? ticketUrl;
  final double? latitude;
  final double? longitude;
  final String? imageUrl;
  final List<String> tags;

  BlocoEvent({
    required this.id,
    required this.name,
    required this.dateTime,
    required this.description,
    required this.address,
    required this.neighborhood,
    this.ticketPrice,
    this.ticketUrl,
    this.latitude,
    this.longitude,
    this.imageUrl,
    this.tags = const [],
  });

  String get formattedDate {
    const weekdays = [
      'Segunda',
      'Terca',
      'Quarta',
      'Quinta',
      'Sexta',
      'Sabado',
      'Domingo',
    ];
    const months = [
      'Jan',
      'Fev',
      'Mar',
      'Abr',
      'Mai',
      'Jun',
      'Jul',
      'Ago',
      'Set',
      'Out',
      'Nov',
      'Dez',
    ];
    final weekday = weekdays[dateTime.weekday - 1];
    final month = months[dateTime.month - 1];
    return '$weekday, ${dateTime.day} $month';
  }

  String get formattedTime {
    final hour = dateTime.hour.toString().padLeft(2, '0');
    final minute = dateTime.minute.toString().padLeft(2, '0');
    return '${hour}h$minute';
  }

  String get googleMapsUrl {
    if (latitude != null && longitude != null) {
      return 'https://www.google.com/maps/search/?api=1&query=$latitude,$longitude';
    }
    final encodedAddress = Uri.encodeComponent('$address, $neighborhood, Belo Horizonte, MG');
    return 'https://www.google.com/maps/search/?api=1&query=$encodedAddress';
  }

  /// Create a copy of this event with updated coordinates
  BlocoEvent copyWith({
    String? id,
    String? name,
    DateTime? dateTime,
    String? description,
    String? address,
    String? neighborhood,
    String? ticketPrice,
    String? ticketUrl,
    double? latitude,
    double? longitude,
    String? imageUrl,
    List<String>? tags,
  }) {
    return BlocoEvent(
      id: id ?? this.id,
      name: name ?? this.name,
      dateTime: dateTime ?? this.dateTime,
      description: description ?? this.description,
      address: address ?? this.address,
      neighborhood: neighborhood ?? this.neighborhood,
      ticketPrice: ticketPrice ?? this.ticketPrice,
      ticketUrl: ticketUrl ?? this.ticketUrl,
      latitude: latitude ?? this.latitude,
      longitude: longitude ?? this.longitude,
      imageUrl: imageUrl ?? this.imageUrl,
      tags: tags ?? this.tags,
    );
  }
}
